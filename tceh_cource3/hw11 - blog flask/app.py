# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy
import config

__author__ = 'ska'

app = Flask(__name__, template_folder='template')
app.config.from_pyfile(config)
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def main():
    return 'Hello World!'


if __name__ == '__main__':
    from models import *
    db.create_all()
    app.run()
