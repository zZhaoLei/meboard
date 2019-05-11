#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import click

from meboard import app, db


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    '''Initialize the database.'''
    if drop:
        click.confirm('Delete Database?', abort=True)
        db.drop_all()
    db.create_all()
    click.echo('Initialize the database.')
