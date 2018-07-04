from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class TranslateForm(FlaskForm):
    input_text = StringField('Input Text', [DataRequired(), Length(5, 254)], render_kw={"placeholder": "Inform your text to translate", "autofocus": "true"})
