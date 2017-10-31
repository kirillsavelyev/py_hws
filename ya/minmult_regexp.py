'''
Дан массив целых (в том числе отрицательных) чисел.
Нужно на языке Python написать функцию, выдающую минимальное произведение,
которое можно составить из двух чисел этого массива.
'''

# from random import randint
from sys import maxsize


def minMult(l):
    min_item = max_item = l[0]
    min_mult = maxsize
    for item in l[1:]:
        for i in [min_item, max_item]:
            temp_mult = i * item
#             min_mult = min(min_mult, temp_mult)
            if min_mult > temp_mult: min_mult = temp_mult
#         min_item = min(min_item, item)
#         max_item = max(max_item, item)
        if min_item > item: min_item = item
        if max_item < item: max_item = item

    return min_mult

# L = [randint(-100, 100) for i in range(30)]

# print (minmult(L))


'''
В системе авторизации есть ограничение: 
логин должен состоять из латинских букв, цифр, точки и минуса, 
начинаться с буквы и заканчиваться только буквой или цифрой; 
минимальная длина логина — один символ, максимальная — 20 символов. 
Напишите код на языке Python, проверяющий соответствие 
входной строки этому правилу.
'''

import re


def lognameValidation(login):
    result = re.match(r'^([a-z]{1}|[a-z]{1}[\w.-]{0,18}\w{1})$', login)
    return '{} login name'.format('Incorrect' if result == None else 'Correct')

# print(lognameValidation('s'))
# print(lognameValidation('super-puper.druper'))
# print(lognameValidation('super-puper.druper2'), end='\n\n')
# print(lognameValidation('super-puper$druper2'))
# print(lognameValidation('super-megapuper.druper3'))
# print(lognameValidation('-megapuper.druper4'))
# print(lognameValidation('megapuper.druper4-'))
# print(lognameValidation(''))
