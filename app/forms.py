from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ReivewTextForm(FlaskForm):
    review_text = TextAreaField('Review', validators=[DataRequired()])
    submit = SubmitField('Post')
    