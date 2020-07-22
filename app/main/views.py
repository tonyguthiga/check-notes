from flask_login import login_required
from . import main
from flask import render_template,url_for,request,redirect,abort
from ..models import User,Category
from .. import db
from .forms import UpdateProfile,CategoryForm

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

@main.route('/add/category', methods=['GET', 'POST'])
@login_required
def new_category():
    form = CategoryForm()
    if form.validate_on_submit():
        name = form.name.data
        new_category = Category(name = name)
        new_category.save_category()

        return redirect(url_for('.profile'))
    title = 'New Category'
    return render_template('new_category.html', category_form = form, title = title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))
    return render_template("profile/update.html", form = form)