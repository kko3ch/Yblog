from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required,Email

class Post_Form(FlaskForm):
    title = StringField('Title', validators=[Required()])
    author = StringField('Author', validators=[Required()])
    content = TextAreaField('Write', validators=[Required()])   
    submit = SubmitField('Post')

class Update_Profile(FlaskForm):
    bio = TextAreaField('Add something more about Yourself...', validators = [Required()])
    submit = SubmitField('Submit')
    
class CommentsForm(FlaskForm):
   comment = TextAreaField('Leave a comment',validators=[Required()])
   alias = StringField('Alias',validators=[Required()])
   submit = SubmitField('Add Comment')