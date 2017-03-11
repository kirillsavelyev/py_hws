# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
import locale
import os
from settings import APP_ROOT


class NewUserForm(FlaskForm):
	email = StringField(label='E-mail', validators=[
		validators.length(min=6, max=35),
		validators.DataRequired(),
		validators.Email(message='Invalid e-mail')
	])
	password = PasswordField(label='Password', validators=[
		validators.length(min=6),
		validators.DataRequired(),
		validators.equal_to('confirm', message='Pass not match')
	])
	confirm = PasswordField(label='Repeat password')


app = Flask(__name__)
app.config.from_pyfile('settings.py')


@app.route("/")
def home():
	return "Hello World!"


@app.route("/locales/")
def locales():
	locs = ['ru', 'en', 'it']
	locales_dict = {l: locale.locale_alias[l] for l in locs}
	return jsonify(locales_dict)


@app.route("/sum/<int:first>/<int:second>/")
def summ(first, second):
	return str(first + second)


@app.route("/greet/<user_name>/")
def greet(user_name):
	return "Hello, %s" % user_name


@app.route("/form/user/", methods=['GET', 'POST'])
def new_user():
	form = NewUserForm(request.form)
	if request.method == 'POST':
		if form.validate():
			return jsonify({'status': 0, 'errors': form.errors})
		else:
			return jsonify({'status': 1, 'errors': form.errors})
	else:
		return render_template("register.html", form=form)


@app.route("/serve/<path:filename>")
def return_file(filename):
	try:
		with open(os.path.join(APP_ROOT, 'files', filename), 'r') as f:
			return f.read()
	except FileNotFoundError as e:
		return render_template('404.html'), 404

if __name__ == "__main__":
	app.run()