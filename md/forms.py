from random import choices
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired
from md import util


class InfoForm(FlaskForm):
    capShape = SelectField('Cap-Shape', choices=util.get_att()['cap-shape'])
    capColor = SelectField('Cap-Color', choices=util.get_att()['cap-color'])
    bruises = SelectField('Bruises', choices=util.get_att()['bruises'])
    odor = SelectField('Odor', choices=util.get_att()['odor'])
    gillSize = SelectField('Gill Size', choices=util.get_att()['gill-size'])
    gillColor = SelectField('Gill-color', choices=util.get_att()['gill-color'])
    stalkRoot = SelectField('Stalk Root', choices=util.get_att()['stalk-root'])
    ringType = SelectField('Ring type', choices=util.get_att()['ring-type'])
    spc = SelectField('Spore Print Color', choices=util.get_att()['spore-print-color'])
    population = SelectField('Population', choices=util.get_att()['population'])
    
    submit = SubmitField('Is it safe?')


