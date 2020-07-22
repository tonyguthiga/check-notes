from flask_login import login_required,current_user
from . import main
from flask import render_template,url_for,request,redirect,abort
from ..models import User,Category,Note
from .. import db
from .forms import UpdateProfile,NoteForm

@main.route('/')
def index():
    title = 'Home - Welcome'
    return render_template('index.html', title=title)

@main.route('/add',methods =['GET','POST'])
@login_required
def add_note():
    form = NoteForm()

    if form.validate_on_submit():
        note = Note(title = form.title.data, note = form.pitch.data,user=current_user)
        
        db.session.add(note)
        db.session.commit()

        return redirect(url_for('main.profile'))
         
    return render_template('add.html',note_form=form)


@main.route('/categories/<int:id>')
def categories(id):
    category = Category.query.get(id)
    if category is None:
        abort(404)

    return render_template('category.html', category=category)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    notes = Note.query.order_by(Note.time.desc()).all()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,notes=notes)

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