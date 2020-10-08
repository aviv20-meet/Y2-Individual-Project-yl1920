import datetime
from sqlalchemy import Column, DateTime, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin

Base = declarative_base()


class Post(Base):
   __tablename__ = 'posts'
   id = Column(Integer, primary_key=True)
   title = Column(String)#The name of the post
   content = Column(String)#The post contents
   auther_id = Column(Integer) # The user ID of the post's auther 
   comments_id = Column(Integer) #id of table comments 
   date_posted  = Column(DateTime, default=datetime.datetime.utcnow) #Time of post upload
   post_time = Column(String) #Time pf post on the timeline


class Comment(Base):
	__tablename__ = 'comments'
	id = Column(Integer, primary_key=True)
	time_upload = Column(String) #Time of post upload
	comment_text = Column(String)#The post contents
	auther = Column(Integer) # User Id of the comment's auther 
	post_id = Column(Integer) #id of table comments 

class User(Base , UserMixin):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	username = Column(String(15), unique=True)
	email = Column(String(50), unique=True)
	password = Column(String(80))

		
