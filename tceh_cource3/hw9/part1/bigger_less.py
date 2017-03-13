# -*- coding: utf-8 -*-

from flask import Flask
import random


__author__ = 'ska'


class GameHandler(object):
    def __init__(self, max_num):
        self.max_num = max_num
        self.q_number = None
        self.guessed = 0

    def gen_num(self):
        self.q_number = random.randint(0, self.max_num)

    def add_win(self):
        self.guessed += 1
        return self.guessed


app = Flask(__name__)


def thermometer(qn, tn):
    max_num = game_handler.max_num
    temp = abs(qn - tn)
    if temp >= max_num/2:
        return u'Холодно. '
    elif temp >= max_num/4:
        return u'Тепло! '
    else:
        return u'Горячо!!! '


@app.route('/')
def main():
    return u'Начнем игру "Угадай число". ' \
           u'Добавь / и цифру от 0 до %d в конце URL-адреса.' % game_handler.max_num


@app.route('/<int:try_num>')
def game(try_num):
    q_number = game_handler.q_number
    if try_num < q_number:
        return thermometer(q_number, try_num) + u'Больше'
    elif try_num > q_number:
        return thermometer(q_number, try_num) + u'Меньше'
    elif try_num == q_number:
        win_total = game_handler.add_win()
        game_handler.gen_num()
        return u'Угадал! Да ты {0}! Угадал {1} раз(а)! ' \
               u'Я хочу отыграться и загадываю новое число! Играем!'.\
            format(random.choice(['снайпер', 'везунчик', 'упёртый']), win_total)
    else:
        return u'Градусник разбился...'


if __name__ == '__main__':
    game_handler = GameHandler(100)
    game_handler.gen_num()
    app.run(host='localhost', port=4000)
