from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class NoteForm(FlaskForm):
    title = StringField('Pitch title',validators=[Required()])
    pitch = TextAreaField('Pitch')
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CategoryForm(FlaskForm):
    name = StringField('Category Name', validators=[Required()])
    submit = SubmitField('Submit')