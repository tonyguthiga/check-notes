from flask_login import UserMixin
from . import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash


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

