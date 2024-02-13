from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired()])
    content = TextAreaField('내용', validators=[DataRequired()])

class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[
    DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])
    pnumber = StringField('휴대폰번호', validators=[DataRequired(), Length(min=10, max=11)])
    Hadress = StringField('집주소', validators=[DataRequired(), Length(min=1, max=40)])
    pcode = StringField('우편번호', validators=[DataRequired()])
    Cadress = StringField('회사주소', validators=[DataRequired()])
    Clitype = SelectField('고객타입', choices=[('1','고객1')], validators=[DataRequired()])
    Ncode = StringField('국가', validators=[DataRequired()])

class loginForm(FlaskForm):
    username = StringField('아이디', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])   

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired()])




