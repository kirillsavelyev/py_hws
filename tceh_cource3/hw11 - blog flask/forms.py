# -*- coding: utf-8 -*-

from wtforms_alchemy import ModelForm
from models import Post

__author__ = 'kirillsavelyev'


class PostForm(ModelForm):
    class Meta:
        model = Post
        include = [
            'user_id',
        ]
