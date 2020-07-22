from flask_login import login_required
from . import main
from flask import render_template,url_for,request,redirect,abort
from ..models import User
from .. import db

@main.route('/')
def index():
    title = 'Home - Welcome'
    return render_template('index.html', title=title)

@main.route('/categories/<int:id>')
def categories(id):
    category = Category.query.get(id)
    if category is None:
        abort(404)

    return render_template('category.html', category=category)
