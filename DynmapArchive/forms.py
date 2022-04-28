from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField, FieldList,FormField
from wtforms.validators import InputRequired,Optional
from wtforms.fields.html5 import DateField
import os

if os.name == 'nt':
    s = "#"
else:
    s = "-"

class TownForm(FlaskForm):
    town = StringField(validators=[InputRequired()], render_kw={'class':'form-control', 'placeholder':'Town Name'})

class TownMapForm(FlaskForm):
  date = DateField(format=F"%Y-%m-%d", validators=[InputRequired()], render_kw={'class':'form-control'})
  datetwo = DateField('End Date (Optional)', format=F"%Y-%m-%d", validators=[Optional()],
                      render_kw={'class': 'form-control'})
  town = FieldList(FormField(TownForm), min_entries=1, validators=[Optional()])
  addrow = SubmitField('+', render_kw={'class':'btn btn-primary'})
  delrow = SubmitField('-', render_kw={'class':'btn btn-primary'})
  submit = SubmitField('Render', render_kw={'class':'btn btn-primary'})

class NationMapForm(FlaskForm):
  date = DateField(format=F"%Y-%m-%d", validators=[InputRequired()], render_kw={'class':'form-control'})
  datetwo = DateField('End Date (Optional)', format=F"%Y-%m-%d", validators=[Optional()],
                      render_kw={'class': 'form-control'})
  town = StringField(validators=[InputRequired()], render_kw={'class':'form-control', 'placeholder':'Nation Name'})
  submit = SubmitField('Render', render_kw={'class':'btn btn-primary'})

class SearchForm(FlaskForm):
  date = DateField(format=F"%Y-%m-%d", validators=[InputRequired()], render_kw={'class':'form-control'} )
  query = StringField('', validators=[InputRequired()], render_kw={'class':'form-control', 'placeholder':'Search Term'})
  qsubmit = SubmitField("Search", render_kw={'class':'btn btn-primary'} )