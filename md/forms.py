from random import choices
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired
from md import util


class InfoForm(FlaskForm):
    capShape = SelectField('Cap-Shape', choices=util.__attributes['cap-shape'])
    capColor = SelectField('Cap-Color', choices=util.__attributes['cap-color'])
    bruises = SelectField('Bruises', choices=util.__attributes['bruises'])
    odor = SelectField('Odor', choices=util.__attributes['odor'])
    gillSize = SelectField('Gill Size', choices=util.__attributes['gill-size'])
    gillColor = SelectField('Gill-color', choices=util.__attributes['gill-color'])
    stalkRoot = SelectField('Stalk Root', choices=util.__attributes['stalk-root'])
    ringType = SelectField('Ring type', choices=util.__attributes['ring-type'])
    spc = SelectField('Spore Print Color', choices=util.__attributes['spore-print-color'])
    capShape = SelectField('Population', choices=util.__attributes['population'])
    
    submit = SubmitField('Is it safe?')


