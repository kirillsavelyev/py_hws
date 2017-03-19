# -*- coding: utf-8 -*-

from datetime import date
from app import db

__author__ = 'kirillsavelyev'

tag_post = db.Table(
    'tag_post',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User {0}>'.format(self.username)

    def __str__(self):
        return repr(self)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey('user.id'), nullable=False, index=True
    )
    user = db.relationship(
        'User', backref=db.backref('posts', lazy='dynamic')
    )
    title = db.Column(db.String(140), unique=True, nullable=False)
    content = db.Column(db.String(3000), nullable=False)
    date_created = db.Column(db.Date, default=date.today)
    is_visible = db.Column(db.Boolean, default=True)
    slug = db.Column(db.String(300), unique=True, nullable=False)
    tag = db.relationship(
        'Tag', secondary=tag_post, backref=db.backref('posts', lazy='dynamic')
    )

    def __repr__(self):
        return '<Post {0}>'.format(self.title)

    def __str__(self):
        return repr(self)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    post = db.relationship(
        'Post', secondary=tag_post, backref=db.backref('tags', lazy='dynamic')
    )

    def __repr__(self):
        return '<Tag {0}>'.format(self.name)

    def __str__(self):
        return repr(self)
