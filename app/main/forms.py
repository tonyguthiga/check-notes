
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class CategoryForm(FlaskForm):
    name = StringFiled('Category Name', validators=[Required()])

    submit = SubmitField('Submit')