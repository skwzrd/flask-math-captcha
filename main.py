from flask import Flask, render_template, redirect, url_for
from forms import MyForm # required import
import os
from captcha import MathCaptcha # required import

app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route('/', methods=['GET', 'POST'])
def home():
    form = MyForm()
    captcha = MathCaptcha()
    message=None

    if form.validate_on_submit():
        # check is math captcha is valid
        if captcha.is_valid(form.captcha_id.data, form.captcha_answer.data):
            print(form.comment.data) # do <thing> with comment here
            return redirect(url_for('home'))

        message = 'Incorrect answer!'

    # set the form math captcha
    form.captcha_id.data, form.captcha_b64_img_str = captcha.generate_captcha()

    return render_template('home.html', form=form, message=message)

app.run('0.0.0.0', port=5000, debug=True)
