# -*- coding: utf-8 -*-

#Написать декоратор, который отменяет выполнение функции и пишет: ИМЯ_ФУНКЦИИ не будет вызвана
print('01\n')

def cancelRun(func):
	print (func.__name__ + u' не будет вызвана')

@cancelRun
def noPensions():
	print(u"Здоровья вам и хорошего настроения! © ДАМ")


#Реализовать декоратор, который измеряет скорость выполнения функций. Написать три разные функции, задекорировать их и проверить
print('\n02\n')

from time import clock

def measureSpeed(func):

    def wrapper(*args, **kwargs):
        t = clock()
        res = func(*args, **kwargs)
        print (func.__name__ + ' running time:', clock() - t)
        return res
    return wrapper

@measureSpeed
def factorial(n):
	n = int(n)
	fctrl = 1
	i = 0
	while i < n:
		i += 1
		fctrl = fctrl * i

	#print(fctrl)

poem = list('I went down to the river, I set down on the bank. I tried to think but couldn\'t,So I jumped in and sank.')

@measureSpeed
def insertToList(i, item):
	poem.insert(i, item)
	#print ('Ta-daa!')

@measureSpeed
def appendToList(item):
	poem.append(item)
	#print (poem)

factorial(9999)
insertToList(30, 'WOW!')
appendToList('WOW!')


#Написать генероторное выражение, которое включает в себя все четные числа от 0 до 100
print('\n03\n')

generator = (x for x in range(2, 101, 2))
print(list(generator))


#Написать генератор, который возвращает бесконечную последовательность случайных чисел, таких что следующее не меньше прошлого
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

#Быстро работает, но рамдомна только часть числа в последовательности
print('\n04\n')

from random import random

def randomInfinity():
	t = 0
	while True:
		tmp = random() 
		t += tmp
		yield t

ri = randomInfinity()

for i in range(10):
	print(next(ri))


#Написать генератор, который принимает на вход дату и на каждый вызов выдает следующий день
print('\n05\n')

from datetime import date, timedelta

def nexDayGenerator(y, m, d):
	day = date(y, m, d)
	while True:
		day += timedelta(days=1)
		yield day

nd = nexDayGenerator(2017, 2, 23)

for i in range(10):
	print (next(nd))
