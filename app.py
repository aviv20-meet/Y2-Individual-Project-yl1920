#All imports for this file

#Imports for the flask libraries
from flask import Flask,flash
from flask import render_template ,redirect , url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bootstrap import Bootstrap

#Imports from the local file databases.py
from databases import get_all_posts , get_post , get_user , add_user

#Imports for the local file forms.py
from forms import Login_form , Register_form

#imports for the werkzeug Library 
from werkzeug.security import generate_password_hash, check_password_hash

#imports for os commands
import os

#init app setup
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

#setup user loader
@login_manager.user_loader
def load_user(user_id):
    return get_user(int(user_id))

#login page function and route
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login_form()
    if form.validate_on_submit():
        user = get_user(form.username.data)
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                print("Login Successful")
                return redirect(url_for('dashboard'))
        print("Login Failed")
        return None
        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login_page.html', form=form,title1 = "Login")

#main page timeline with all posts function and route
@app.route('/')
def main_timeline():
    return render_template('main_timeline.html',posts = get_all_posts(),title1 = "The Timeline")

#signup page function and route
#TODO_test sigup
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = Register_form()

    if form.validate():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        add_user(form.username.data, form.email.data, hashed_password)

        return redirect(url_for('dashboard'))
        #return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('signup_page.html', form=form,title1 = "Sign Up")

#??????????
@app.route('/test')
def test():
	form = Login_form()
	return render_template("login.html", form = form)

#user dashboard(login required) function and route
@app.route('/dashboard')
@login_required
def dashboard():
    posts = get_all_posts()
    for post in posts:
    	if post.user_id != current_user.id:
    		post.pop()
    render_template('dashboard.html', posts = posts)

#Post page function and route
@app.route('/post:<id>')
def load_post(id):
	return render_template("post_page.html",posts = [get_post(id)],title1 =get_post(id).post_name)

#run app on file complition 
if __name__ == '__main__':
	app.run(debug = True)
