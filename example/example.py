import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # required for this example app

from flask import Flask, render_template, redirect, url_for
from forms import MyForm
from captcha import MathCaptcha

app = Flask(__name__)
app.secret_key = "123456" # change me
app.config["MATH-CAPTCHA-FONT"] = os.path.join(os.path.dirname(__file__), "../fonts/tly.ttf")


@app.route("/", methods=["GET", "POST"])
def home():
    form = MyForm()
    captcha = MathCaptcha(tff_file_path=app.config["MATH-CAPTCHA-FONT"])
    message = None

    if form.validate_on_submit():
        # check is math captcha is valid
        if captcha.is_valid(form.captcha_id.data, form.captcha_answer.data):
            # do <thing> with form data
            return redirect(url_for("home"))

        message = "Incorrect answer!"

    # set the form math captcha
    form.captcha_id.data, form.captcha_b64_img_str = captcha.generate_captcha()

    return render_template("home.html", form=form, message=message)


app.run("0.0.0.0", port=5000, debug=True)
