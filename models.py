from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from config import Config
from database import Base
from flask_security import UserMixin, RoleMixin
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Boolean, DateTime, Column, Integer, \
    String, ForeignKey
import datetime

app = Flask(__name__)
# set up the configurations
app.config.from_object(Config)
# set up sql alchemy
db = SQLAlchemy(app)
# import from database base
migrate = Migrate(app, Base)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


class RolesUsers(Base):
    __tablename__ = 'roles_users'
    id = Column(Integer(), primary_key=True)
    user_id = Column('user_id', Integer(), ForeignKey('user.id'))
    role_id = Column('role_id', Integer(), ForeignKey('role.id'))


class Role(Base, RoleMixin):
    __tablename__ = 'role'
    id = Column(Integer(), primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255))


class User(Base, UserMixin):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True)
    password = Column(String(255))
    first_name = Column(String(64), index=True)
    second_name = Column(String(64), index=True)
    email = Column(String(255), unique=True, nullable=False)
    phone_number = Column(String(20), nullable=True)
    active = Column(Boolean, default=False)
    # photographer = relationship("Photographer", uselist=False, back_populates="user")
    date_created = Column(DateTime, default=datetime.datetime.utcnow)
    roles = relationship('Role', secondary='roles_users',
                         backref=backref('users', lazy='dynamic'))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    # def is_photographer(self):
    #     return True if self.photographer else False


"""
class Photographer(Base):
    __tablename__ = "photographer"
    id = Column(Integer, primary_key=True)
    user = relationship('User', back_populates='photographer')
    photos = relationship("Photo", backref='person', lazy=True)

    def __repr__(self):
        return '<Photographer {}>'.format(self.user.username)


class Photo(Base):
    __tablename__ = "photo"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), index=True, unique=True)
    photographer_id = Column(Integer, ForeignKey("photographer.id"), index=True)
    date_added = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<Photo {}>'.format(self.name)
"""

if __name__ == '__main__':
    manager.run()
