from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class SubmitForm(FlaskForm):
    """Submit form."""

    title = StringField(
        "Title", validators=[DataRequired(message="Please enter a title.")]
    )
    url = StringField(
        "URL", validators=[DataRequired(message="Please enter a URL.")]
    )

    tags = StringField("Tags")

    pin = PasswordField(
        "PIN", validators=[DataRequired(message="Please enter the PIN.")]
    )
    submit = SubmitField("Submit")
