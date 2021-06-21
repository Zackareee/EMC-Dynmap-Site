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
    town = StringField(validators=[InputRequired()])

class MapForm(FlaskForm):
  date = DateField('Start Date',format=F"%Y-%m-%d")
  town = FieldList(FormField(TownForm), min_entries=1, validators=[Optional()])
  datetwo = DateField('End Date (Optional)',format=F"%Y-%m-%d", validators=[Optional()])
  addrow = SubmitField('Add row')
  delrow = SubmitField('Delete row')
  submit = SubmitField("Render Town(s)")


class SearchForm(FlaskForm):
  date = DateField('Date', validators=[InputRequired()])
  query = StringField('Query (Case Sensitive)', validators=[InputRequired()])
  qsubmit = SubmitField("Find Town(s)")

