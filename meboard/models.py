#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from datetime import datetime
from meboard import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.now, index=True)
