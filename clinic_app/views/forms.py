"""
Module contains form classes for posting data on app's web pages.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Email, Length, EqualTo


class CustomEmail(Email):
    """Extended email validator that in addition allows using 'root' as email."""
    def __call__(self, form, field):
        if not field.data == 'root':
            super().__call__(form, field)


pass_length = Length(min=6, max=40)


class LoginForm(FlaskForm):
    """Form for logging users in"""
    email = StringField('Email: ', validators=[CustomEmail()])
    pwd = PasswordField('Password: ', validators=[InputRequired(), pass_length])
    remember = BooleanField('Remember me', default=False)
    submit = SubmitField('Log in')


class ChangePassForm(FlaskForm):
    """Form for changing user's password"""
    password = PasswordField('Current password: ', validators=[InputRequired(), pass_length])
    new_pass = PasswordField('New password: ', validators=[
        InputRequired(),
        EqualTo('confirm', message='Passwords must match'),
        pass_length
    ])
    confirm = PasswordField('Confirm password: ')
    submit = SubmitField('Submit change')
