# -*- coding: utf-8 -*-

import requests
import json
import re


""" реализовать две функции: write_to_file(data) и read_file_data()"""


def write_to_file(text):
	with open('hw7_wtf.txt', 'w') as f:
		f.write(text)


def read_file_data():
	with open('hw7_wtf.txt', 'r') as f:
		text = f.read()
		print('Вы ввели: ', text, end='\n\n')


""" получать при помощи requests данные сайта https://jsonplaceholder.typicode.com/,
выводить в консоль все пары "ключ-значение", сохранять полученный json в файл"""


def get_json(url):
	r = requests.get(url)
	for key, value in r.headers.items():
		print(key, ':', value)
	print()

	with open('headers.json', 'w') as j:
		j.write(json.dumps(dict(r.headers)))


"""Обратиться с странице https://habrahabr.ru/. Получить текст страницы.
При помощи регулярных выражений нужно получить все ссылки со страницы на другие."""


def get_urls_from_url(url):
	body = requests.get(url).content

	urls = re.findall(r'(?<=<a href=")http[s]?://[^"]*', str(body))

	for u in urls:
		print(u)


if __name__ == '__main__':
	write_to_file(input('Введите текст для записи: '))
	read_file_data()
	get_json('https://jsonplaceholder.typicode.com/')
	get_urls_from_url('https://habrahabr.ru/')