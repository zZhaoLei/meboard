#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from meboard import app


@app.route('/')
def index():
    return 'this is index.'
