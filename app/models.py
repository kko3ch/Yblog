from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import login_manager
from . import db

class User(UserMixin,db.Model):
    '''
    Class User defines users as objects
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    firstname = db.Column(db.String(255),index = True)
    lastname = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    profile_photo = db.relationship('PhotoProfile',backref = 'user',lazy = "dynamic")
    posts = db.relationship('Post', backref='user', lazy='dynamic')
    comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.username}'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class PhotoProfile(db.Model):
    __tablename__ = 'profile_photos'

    id = db.Column(db.Integer,primary_key = True)
    pic_path = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

class Post(db.Model):
    '''
    Movie class to define blog post Objects
    '''
    __tablename__ = 'post'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    content = db.Column(db.String) 
    post_pic_path = db.Column(db.String())
    post_pic = db.relationship('PostPhoto',backref = 'user',lazy = "dynamic")
    comments = db.relationship('Comment',backref = 'pitch',lazy = 'dynamic')
    posted = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Post {self.post}'

class PostPhoto(db.Model):
    '''
    class that defined a blog's image
    '''
    __tablename__ = 'blog_photos'
    id = db.Column(db.Integer,primary_key = True)
    post_pic_path = db.Column(db.String())
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))

class Comment(db.Model):
    '''
    Comments class to define comment objects
    '''
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String)
    posted = db.Column(db.Time,default=datetime.utcnow())
    post_id = db.Column(db.Integer,db.ForeignKey('post.id'))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'comment:{self.comment}'

class Quote:
    '''
    class that creates instance of quotes
    '''
    def __init__(self,id,author,quote):
        '''
        function to create the NewsSource instance
        '''
        self.id = id
        self.author = author
        self.quote = quote
    