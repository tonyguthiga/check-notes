from flask_login import login_required
from . import main

@main.route('/notes/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id)

@main.route('/categories/<int:id>')
def categories(id):
    category = Category.query.get(id)
    if category is None:
        abort(404)

    return render_template('category.html', category=category)
