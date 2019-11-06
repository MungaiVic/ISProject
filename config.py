import os

basedir = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = 'C:/Users/User/Documents/Strathmore/ICS/Academic Work/Year 2/Semester 2/IS Project/photography/static'
CLIENT_FOLDER = 'C:/Users/User/Documents/Strathmore/ICS/Academic Work/Year 2/Semester 2/IS Project/photography/static/Client_Uploads'


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = 'secret123'
    SECURITY_PASSWORD_SALT = 'super-secret-random-salt'

    # config MYSQL
    MYSQL_HOST = '127.0.0.1'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'photography'
    MYSQL_CURSORCLASS = 'DictCursor'

    # smtp
    MAIL_SERVER = 'stmp.goolemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

    # config image format
    UPLOAD_FOLDER = UPLOAD_FOLDER
    CLIENT_FOLDER = CLIENT_FOLDER
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024

    SECURITY_RECOVERABLE = True
    SECURITY_REGISTERABLE = True
