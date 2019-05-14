#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class LeavForm(FlaskForm):
    name = StringField('标题', validators=[DataRequired(), Length(1, 20)])
    body = TextAreaField('内容', validators=[DataRequired(), Length(1,200)])
    submit = SubmitField('发布')
