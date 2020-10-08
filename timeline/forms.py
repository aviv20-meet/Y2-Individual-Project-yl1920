#All imports for this file

#import from local databases.py file

from timeline.databases import get_all_usernames, get_all_user_emails

#Imports for the flask libraries
from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Email, Length, NoneOf, EqualTo

#creates the Login form using flask_wtf and FlaskForm
class Login_form(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

#creates the Register New User form using flask_wtf and FlaskForm
class Register_form(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50),NoneOf(get_all_user_emails(),message='That email adress is taken. Please choose a diffrent one.')])
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15),NoneOf(get_all_usernames(),message='The username is taken. Please choose a diffrent one.')])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('Password')])
    submit = SubmitField('Sign Up')


#creates the Make New Post form using flask_wtf and FlaskForm
#TODOclass Creat_post(FlaskForm):
