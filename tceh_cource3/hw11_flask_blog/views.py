# -*- coding: utf-8 -*-

from slugify import slugify
from flask import (
    Blueprint,
    redirect,
    url_for,
    flash,
    request,
    render_template
)
from forms import PostForm
from models import User, Post
from app import db

__author__ = 'kirillsavelyev'

blog = Blueprint('blog', __name__)


@blog.route('/', methods=['GET', 'POST'])
def main():
    return 'Hello world!'