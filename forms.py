from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, StringField, HiddenField
from wtforms.validators import InputRequired


class MyForm(FlaskForm):
    comment = TextAreaField("Comment:", validators=[InputRequired()])

    captcha_id = HiddenField(validators=[InputRequired()])
    captcha_answer = StringField("Solve the math captcha:", validators=[InputRequired()])
