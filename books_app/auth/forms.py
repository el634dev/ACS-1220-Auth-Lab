from flask_wtf import FlaskForm
from books_app.extensions import app, db, bcrypt
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from books_app.models import User

class SignUpForm(FlaskForm):
    """Sign Up Form"""
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    # Password
    password = PasswordField('Password', validators=[DataRequired()])
    # Submit
    submit = SubmitField('Sign Up')

    # -----------------------------------
    def validate_username(self, username):
        """Validate a user's username"""
        user = User.query.filter_by(username=username.data).first()
        # Check user
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')


# ----------------------
class LoginForm(FlaskForm):
    """Sign Up Form"""
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    # Password
    password = PasswordField('Password', validators=[DataRequired()])
    # Submit
    submit = SubmitField('Log In')

    # -----------------------------------
    def validate_username(self, username):
        """Validate a user's username"""
        user = User.query.filter_by(username=username.data).first()

        if not user:
            raise ValidationError('No user with that username. Please try again.')

    # --------------------------------
    def validate_password(self, password):
        """Validate a user's password"""
        user = User.query.filter_by(username=self.username.data).first()

        if user and not bcrypt.check_password_hash(
                user.password, password.data):
            raise ValidationError('Password doesn\'t match. Please try again.')
