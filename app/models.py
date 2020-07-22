from . import db

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
