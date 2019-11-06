from flask_security.forms import RegisterForm
from wtforms import StringField, validators


# registration form
class RegistrationForm(RegisterForm):
    first_name = StringField('first_name', [validators.length(min=2, max=50)])
    second_name = StringField('second_name', [validators.length(min=2, max=50)])
    phone_number = StringField('phone_number', [validators.length(min=10, max=12)])
    username = StringField('username', [validators.length(min=6, max=30)])
