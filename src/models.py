import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class MyEnum(enum.Enum):
    pictures = 1
    videos = 2
    stories = 3

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable= False)
    firstname = Column(String(250), nullable= False)
    lastname = Column(String(250), nullable= False)
    email = Column(String(250), nullable= False)

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    followed_by = Column(Integer, ForeignKey('user.id'))
    following = Column(Integer, ForeignKey('user.id'))

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable= False)
    autor_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    url = Column(String(250), nullable= False)
    post_id = Column(Integer, ForeignKey('post.id'))
    tipo = Column(Enum(MyEnum))

    


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
