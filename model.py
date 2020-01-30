from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin

Base = declarative_base()


class Post(Base):
   __tablename__ = 'posts'
   id = Column(Integer, primary_key=True)
   post_name = Column(String)#The name of the post
   post_text = Column(String)#The post contents
   user_id = Column(Integer) # User Id of the Poster 
   comments_id = Column(Integer) #id of table comments 
   time_upload = Column(String) #Time of post upload
   time_post = Column(String) #Time pf post on the timeline


class Comment(Base):
	__tablename__ = 'comments'
	id = Column(Integer, primary_key=True)
	time_upload = Column(String) #Time of post upload
	comment_text = Column(String)#The post contents
	user_id = Column(Integer) # User Id of the Poster 
	post_id = Column(Integer) #id of table comments 

class User(Base , UserMixin):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	username = Column(String(15), unique=True)
	email = Column(String(50), unique=True)
	password = Column(String(80))

		
