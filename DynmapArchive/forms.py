from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField, FieldList,FormField
from wtforms.validators import InputRequired,Optional
from wtforms.fields.html5 import DateField

class TownForm(FlaskForm):
    town = StringField(validators=[InputRequired()])

class MapForm(FlaskForm):
  date = DateField('Start Date')
  town = FieldList(FormField(TownForm), min_entries=1, validators=[Optional()])
  datetwo = DateField('End Date (Optional)', validators=[Optional()])
  addrow = SubmitField('Add row')
  delrow = SubmitField('Delete row')
  submit = SubmitField("Render Town(s)")


class SearchForm(FlaskForm):
  date = DateField('Date', validators=[InputRequired()])
  query = StringField('Query (Case Sensitive)', validators=[InputRequired()])
  qsubmit = SubmitField("Find Town(s)")

