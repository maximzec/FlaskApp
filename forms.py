from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField ,BooleanField
from wtforms.validators import DataRequired , Length , Email , EqualTo


class RegistrationForm(FlaskForm):
    first_name = StringField('first_name' , validators=[DataRequired()] , render_kw={"placeholder" : "Ваше имя"})
    last_name = StringField('last_name' , validators=[DataRequired()] , render_kw={"placeholder" : "Ваша фамидия"})
    email = StringField('email' , validators=[DataRequired()], render_kw={"placeholder" : "Ваш Email"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder" : "Пароль"})
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('Password')],render_kw={"placeholder" : "Повторите пароль"})

    submit = SubmitField('Sign Up' , render_kw={'placeholder':'Зарегестрхироваться'})


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

