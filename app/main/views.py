from flask import render_template,request,redirect,url_for,abort
from ..models import Reviews, User
from .forms import ReviewForm,UpdateProfile
from .. import db
#.....
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))
    return render_template("profile/profile.html", form = form)

