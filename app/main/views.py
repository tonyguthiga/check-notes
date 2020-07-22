from . import main




@main.route('/categories/<int:id>')
def categories(id):
    category = Category.query.get(id)
    if category is None:
        abort(404)

    return render_template('category.html', category=category)