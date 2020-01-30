from model import Base, Post, Comment ,User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def make_session():
	engine = create_engine('sqlite:///database.db')
	Base.metadata.create_all(engine)
	DBSession = sessionmaker(bind=engine)
	session = DBSession()
	return session

def get_all_posts():
	session = make_session()
	posts = session.query(
		Post).all()
	return posts

def add_post(post_name,post_text,user_id,comments_id,time_upload,time_post):
	session = make_session()
	post_object = Post(
		post_name = post_name,
		post_text = post_text,
		user_id = user_id,
		comments_id = comments_id,
		time_upload = time_upload,
		time_post = time_post)
	session.add(post_object)
	session.commit()
def delete_post(id):
	session = make_session()
	post = session.query(Post).filter(Post.id == id).delete()
	session.commit()

#edit post's name or 	
def edit_post(id,post_name,post_text):
	session = make_session()
	post = session.query(Post).filter(Post.id == id).first()
	if(post_name != None):
		post.post_name = post_name
	if(post_text != None):
		post.post_text = post_text
	session.commit()

def get_post(id):
	session = make_session()
	post = session.query(Post).filter(Post.id == id).first()
	return post


def add_user(username,email,password):
	session = make_session()
	user_object = User(
		username = username,
		email = email,
		password = password)
	session.add(user_object)
	session.commit()
def get_user(username, id = None):
	session = make_session()
	if id == None:
		user = session.query(User).filter(User.username == username).first()
		return user 
	if(username == None and id != None):
		return session.query(User).filter(User.id == id).first

	return None


#add_post(" Example Post" , "Example contents", 3,1,"13:00:00", "1929")
#add_post("post", "post contents", 3,1, "13:00:00","1929")
#delete_post(1)