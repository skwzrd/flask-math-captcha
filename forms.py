from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, StringField, HiddenField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    comment = TextAreaField("Comment:", validators=[DataRequired()])
    
    captcha_id = HiddenField(validators=[DataRequired()])
    captcha_answer = StringField("Solve the math captcha:", validators=[DataRequired()])
