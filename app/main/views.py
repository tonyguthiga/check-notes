from flask_login import login_required,current_user
from . import main
from flask import render_template,url_for,request,redirect,abort
from ..models import User,Category,Note
from .. import db
from .forms import UpdateProfile,NoteForm,CategoryForm


@main.route('/')
def index():
    title = 'Home - Welcome'
    return render_template('index.html', title=title)

@main.route('category/add-note/<int:id>',methods =['GET','POST'])
@login_required
def add_note(id):
    form = NoteForm()
    category = Category.query.filter_by(id=id).first 

    if category is None:
        abort(404)

    if form.validate_on_submit():
        note = Note(title = form.title.data, note = form.pitch.data)
        
        db.session.add(note)
        db.session.commit()

        return redirect(url_for('main.profile',id=category.id))
         
    return render_template('add.html',note_form=form,category=category)


@main.route('/categories/<int:id>')
def categories(id):
    category = Category.query.get(id)
    if category is None:
        abort(404)
    
    notes = Note.query.order_by(Note.time.desc()).all()
    return render_template('category.html', category=category,notes=notes)

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
    notes = Note.query.order_by(Note.time.desc()).all()
    categories = Category.get_categories()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,notes=notes,categories=categories)

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