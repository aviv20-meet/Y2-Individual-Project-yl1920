#All imports for this file

#import from local databases.py file

from databases import get_all_usernames, get_all_user_emails

#Imports for the flask libraries
from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length, NoneOf

#creates the Login form using flask_wtf and FlaskForm
class Login_form(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

#creates the Register New User form using flask_wtf and FlaskForm
class Register_form(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50),NoneOf(get_all_user_emails(),message='Email Already In Use')])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15),NoneOf(get_all_usernames(),message='Username Already In Use')])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

#creates the Make New Post form using flask_wtf and FlaskForm
#TODOclass Creat_post(FlaskForm):
