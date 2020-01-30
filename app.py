from flask import Flask
from flask import render_template ,redirect , url_for
from databases import get_all_posts , get_post , get_user , add_user
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bootstrap import Bootstrap
from forms import Login_form , Register_form
from werkzeug.security import generate_password_hash, check_password_hash
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return get_user(None,int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login_form()

    if form.validate_on_submit():
        user = get_user(form.username.data)
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                print("wowowo")
                return redirect(url_for('dashboard'))

        return '<h1>Invalid username or password</h1>'
        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)
@app.route('/')
def index():
    return render_template('base_template.html',posts = get_all_posts())

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = Register_form()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = add_user(form.username.data, form.email.data, hashed_password)

        return '<h1>New user has been created!</h1>'
        #return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('signup.html', form=form)
@app.route('/test')
def test():
	form = Login_form()
	return render_template("login.html", form = form)


@app.route('/dashboard')
@login_required
def dashboard():
    posts = get_all_posts()
    for post in posts:
    	if post.user_id != current_user.id:
    		post.pop()
    render_template('dashboard.html', posts = posts)

@app.route('/post:<id>')
def load_post(id):
	return render_template("base_post.html",posts = [get_post(id)])
@app.route('/hello')
def hello():
    return 'Hello, World'

if __name__ == '__main__':
	app.run(debug = True)
