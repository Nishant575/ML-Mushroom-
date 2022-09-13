from md import app
from flask import render_template
from md.forms import InfoForm

@app.route("/")
@app.route("/home")
def home():
    form = InfoForm()
    
    return render_template("index.html", form=form)

