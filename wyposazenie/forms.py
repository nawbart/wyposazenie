from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, DateField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional
from wyposazenie.models import Miejsca, Osoby, TypyUrzadzen, Urzadzenia


