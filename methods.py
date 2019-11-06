import app
from itsdangerous import TimedJSONWebSignatureSerializer as serial
from flask_mail import Message
import os


def get_reset_token(userid, expires_sec=1800):
    cur = app.mysql.connection.cursor()
    cur.execute('SELECT UserID FROM users')
    rows = cur.fetchall()
    for row in rows:
        user_id = row['UserID']
    app.mysql.connection.commit()
    cur.close()
    s = serial(app.app.config['SECRET_KEY'], expires_sec)
    return s.dumps({userid.get(user_id)}).decode('utf-8')


def verify(token):
    s = serial(app.app.config['SECRET_KEY'])
    try:
        user_id = s.loads(token)['userid']
    except:
        return None
    return user_id


def send_reset_email(user):
    token = get_reset_token(user)
    msg = Message('Password Reset Request', sender='ikariuki741@gmail.com', recipients=[user.get(user.email)])
    msg.body = f'''To reset your password visit the following link:
   {app.url_for('reset_token', token=token, _external=True)}
   If you did not make this request then simple ignore this email and no changes will be made 
   '''
    app.mail.send(msg)


