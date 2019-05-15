#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import flash, redirect, url_for, render_template
from meboard import app, db, bootstrap
from meboard.models import Message
from meboard.forms import LeavForm


@app.route('/', methods=['GET', 'POST'])
def index():
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    form = LeavForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(name=name, body=body)
        db.session.add(message)
        db.session.commit()
        flash('你的消息已经发送给整个世界！')
        return redirect(url_for('index'))
    return render_template('index.html', form=form, messages=messages, bootstrap=bootstrap)
