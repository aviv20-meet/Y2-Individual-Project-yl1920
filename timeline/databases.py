
#All the imports for the file
from datetime import datetime
#imports from the local model.py file
from timeline.model import Base, Post, Comment ,User

#imports for the sqlalchemy libary 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


#Creates the database session
def make_session():
	engine = create_engine('sqlite:///database.db')
	Base.metadata.create_all(engine)
	DBSession = sessionmaker(bind=engine)
	session = DBSession()
	return session

#Gets adn returns all the posts in posts table 
def get_all_posts():
	session = make_session()
	posts = session.query(
		Post).all()
	return posts

#Gets adn returns all the users in User table 
def get_all_users():
	session = make_session()
	users = session.query(
		User).all()
	return users

def get_all_usernames():
	session = make_session()
	users = session.query(User).all()
	usernames = []
	for user in users:
		usernames.append(user.username)
	return usernames

def get_all_user_emails():
	session = make_session()
	users = session.query(
		User).all()
	emails = []
	for user in users:
		emails.append(user.email)
	return emails

#Create a new post instance and add it to the Posts table 
def add_post(title ,content,auther_id,comments_id,post_time):
	session = make_session()
	post_object = Post(
		title = title,
		content = content,
		auther_id = auther_id,
		comments_id = comments_id,
		post_time = post_time)
	session.add(post_object)
	session.commit()

#Find a specific post by ID form the posts table	
def delete_post(id):
	session = make_session()
	post = session.query(Post).filter(Post.id == id).delete()
	session.commit()

#Find a speific post by ID from the Posts table and edit the post text and/or post name 
def edit_post(id,post_name,post_text):
	session = make_session()
	post = session.query(Post).filter(Post.id == id).first()
	if(post_name != None):
		post.post_name = post_name
	if(post_text != None):
		post.post_text = post_text
	session.commit()

#Get a specific post by ID from Posts table 
def get_post(id):
	session = make_session()
	post = session.query(Post).filter(Post.id == id).first()
	return post

#Create a new user instance and add it to the Users table 
def add_user(username,email,password):
	session = make_session()
	user_object = User(
		username = username,
		email = email,
		password = password)
	session.add(user_object)
	session.commit()

#Get a specific user from the User table by id and/or username
def get_user(username = None, id = None):
	session = make_session()
	if (id == None and username != None):
		user = session.query(User).filter(User.username == username).first()
		return user 
	if(username == None and id != None):
		user = session.query(User).filter(User.id == id).first
		return user

	return None


#add_post("Example Post" , "Example contents", 3,1,"1929")
#add_post("post", "post contents", 3,1,"1929")
#delete_post(1)