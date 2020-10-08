#All imports for this file

#Imports for the flask libraries
from flask import Flask

#from flask_bootstrap import Bootstrap

from flask_login import LoginManager

#imports for os commands
import os


#init app setup
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24) #14b06b64c84c888d7025f05fc96327d1
#Not sure I need this
#Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


from timeline import routes
