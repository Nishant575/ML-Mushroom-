
from md import app, util
from flask import render_template, request, url_for
from md.forms import InfoForm


@app.route("/", methods=['POST', 'GET'])
@app.route("/home", methods=['POST', 'GET'])
def home():
    form = InfoForm()
    lst = []
    ans = ""
    col = 2
    if form.validate_on_submit():
        lst.extend([form.capShape.data, form.capColor.data, form.bruises.data, form.odor.data, form.gillSize.data, form.gillColor.data, form.stalkRoot.data, form.ringType.data, form.spc.data, form.population.data])
        ans,col = util.detect(lst)
        
    return render_template("index.html", form=form, lst=lst, ans=ans,col=col)

