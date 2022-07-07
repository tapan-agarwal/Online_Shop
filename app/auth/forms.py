from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional

class SignupForm(FlaskForm):
    """User Signup Form."""
    email = EmailField(label='email', validators=[Email(message='Enter a valid email.'), DataRequired(message="We'll need to be in touch.")])
    password = PasswordField(label='password', validators=[DataRequired(message="We need to make sure it's you!"), Length(min=8, message='Select a stronger password.')])
    confirm = PasswordField(label='confirm password', validators=[DataRequired(message="Don't forget to confirm your password!"), EqualTo('password', message='Passwords must match.')])
    address = TextAreaField('address', validators=[Length(max=200), Optional()])
    terms = BooleanField(label='terms', validators=[DataRequired(message="Make sure you've read this!")])

class LoginForm(FlaskForm):
    """User Login Form."""
    email = EmailField(label='email', validators=[DataRequired(message="Who are you again?"), Email(message='Enter a valid email.')])
    password = PasswordField(label='password', validators=[DataRequired("That doesn't seem right.")])

class EditProfile(FlaskForm):
    """User Edit Form."""
    email = EmailField(label='email', validators=[Email(message='Enter a valid email.'), DataRequired(message="We'll need to be in touch.")])
    password = PasswordField(label='password', validators=[DataRequired("That doesn't seem right.")])
    newpassword = PasswordField(label='password', validators=[Optional(), Length(min=8, message='Select a stronger password.')])
    confirm = PasswordField(label='confirm password', validators=[Optional(), EqualTo('newpassword', message='Passwords must match.')])
    address = TextAreaField('address', validators=[Length(max=200), Optional()])
    delete = SubmitField(label="Delete Account", validators=[Optional()])