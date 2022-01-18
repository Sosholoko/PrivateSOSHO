import flask_wtf
import wtforms
from wtforms import validators as vld

class Twitter(flask_wtf.FlaskForm):
    subject = wtforms.StringField("Which topic to search for ? ")
    location = wtforms.StringField("Where to look for ?  ")
    
    submit = wtforms.SubmitField("Search")

