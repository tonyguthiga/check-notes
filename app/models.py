from flask_login import UserMixin
from . import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    password_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))

    def save_categories(self):
        db.session.add(self)
        db.session.commit()

    @classmethod 
    def get_categories(cls):
        categories = Category.query.all()
        return categories

class Note(db.Model):
    __tablename__='notes'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String())
    content = db.Column(db.String())
    time = db.Column(db.DateTime,default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))

    def save_note(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_notes(cls):
        Note.all_notes.clear()

    @classmethod
    def get_notes(cls, id):
        notes = Note.query.filter_by(category_id=id).all()
        return notes
    
    def __repr__(self):
        return f'User {self.title}'


