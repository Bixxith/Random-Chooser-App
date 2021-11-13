from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class RestaurantForm(FlaskForm):
    searchLocation = StringField("Search Location", validators=[DataRequired()])
    searchKeyWord = StringField("Search Key Word")
    searchRadius = IntegerField("Max Distance in Miles", default=3, validators=[DataRequired()])
    submit = SubmitField("Search")
    
    