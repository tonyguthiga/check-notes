from flask_login import login_required

@main.route('/notes/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id)