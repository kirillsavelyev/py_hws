# -*- coding: utf-8 -*-

from time import process_time
from random import random
from datetime import date, timedelta

# Написать декоратор, который отменяет выполнение функции и пишет: ИМЯ_ФУНКЦИИ не будет вызвана
print('01\n')


def cancelrun(func):
	print(func.__name__ + u' не будет вызвана')


@cancelrun
def nopensions():
	print(u"Здоровья вам и хорошего настроения! © ДАМ")


# Реализовать декоратор, который измеряет скорость выполнения функций. Написать три разные
# функции, задекорировать их и проверить
print('\n02\n')


def measurespeed(func):
	def wrapper(*args, **kwargs):
		t = process_time()
		res = func(*args, **kwargs)
		print(func.__name__ + ' running time:', process_time() - t)
		return res

	return wrapper


@measurespeed
def factorial(n):
	n = int(n)
	fctrl = 1
	m = 0
	while m < n:
		m += 1
	fctrl = fctrl * m
	print(fctrl)


poem = list('I went down to the river, I set down on the bank. I tried to think but couldn\'t,'
			' So I jumped in and sank.')


@measurespeed
def inserttolist(key, item):
	poem.insert(key, item)


# print ('Ta-daa!')


@measurespeed
def appendtolist(item):
	poem.append(item)


# print (poem)

factorial(9999)
inserttolist(30, 'WOW!')
appendtolist('WOW!')

# Написать генероторное выражение, которое включает в себя все четные числа от 0 до 100
print('\n03\n')

generator = (x for x in range(2, 101, 2))
print(list(generator))

# Написать генератор, который возвращает бесконечную последовательность случайных чисел,
# таких что следующее не меньше прошлого
'''
#Мне кажется перемудрил, т.к. генератор долго работает

from random import expovariate

def randomInfinity(x):
	t = 0
	while True:
		tmp = expovariate(abs(x)) 
		if tmp > t:
			t = tmp
			print(t)

randomInfinity(-1)
'''

# Быстро работает, но рамдомна только часть числа в последовательности
print('\n04\n')


def randominfinity():
	t = 0
	while True:
		tmp = random()
		t += tmp
		yield t


ri = randominfinity()

for i in range(10):
	print(next(ri))

# Написать генератор, который принимает на вход дату и на каждый вызов выдает следующий день
print('\n05\n')


def nexdaygenerator(y, m, d):
	day = date(y, m, d)
	while True:
		day += timedelta(days=1)
		yield day


nd = nexdaygenerator(2017, 2, 23)

for j in range(10):
	print(next(nd))
