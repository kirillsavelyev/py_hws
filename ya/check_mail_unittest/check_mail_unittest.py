# -*- coding: utf-8 -*-

__author__ = 'kirillsavelyev'


import re
import unittest


def check_mail(mail):
    # check e-mail fully

    if re.match(r'^[a-z0-9"._!,:-]+@[a-z0-9._-]+\.[a-z]{2,4}$', mail):
        addlist = mail.split('@')
        check1, check2, check3, username, domname = True, True, True, addlist[
            0], addlist[1]
    else:
        # check1, check2, check3, username, domname = False, False, False, False, False
        check1 = check2 = check3 = username = domname = False

    # check account name

    if username:
        q, quotes, point = 0, False, False
        for sym in username:
            if q == 128 or (sym in '!,:' and not quotes) \
                    or (sym == '.' and point) or not re.search(
                r'^[a-z0-9"._!,:-]$', sym):
                check2 = False
                break
            else:
                point = False
            if sym == '"':
                quotes = not quotes
            if sym == '.':
                point = True
            q += 1
        check2 = check2 and not quotes

    # check domain name

    if domname:
        q, dash, point, at = 0, False, False, True
        for sym in domname:
            if q == 256 or (sym == '-' and at) or (sym == '-' and point) \
                    or (sym == '.' and at) or (sym == '.' and dash) \
                    or (sym == '.' and point) or not re.search(r'^[a-z0-9._-]$',
                                                               sym):
                check3 = False
                break
            else:
                at, point, dash = False, False, False
            if sym == '.':
                point = True
            if sym == '-':
                dash = True
            q += 1
        check3 = check3 and q > 2 and sym != '-'

    check = check1 and check2 and check3
    return check


class TestCheckMailFunctions(unittest.TestCase):
    def setUp(self):
        self.mail_values = (
            ('', False),
            ('kirillsavelyev', False),
            ('yandex.ru', False),
            ('ks@ru', False),
            ('ks@.ru', False),
            ('ks@ .ru', False),
            ('ks@' + 'y' * 253 + '.ru', True),
            ('ks@' + 'y' * 254 + '.ru', False),
            ('ks@python.yandex.ru', True),
            ('ks@py-thon.yandex.ru', True),
            ('ks@-python.yandex.ru', False),
            ('ks@python-.yandex.ru', False),
            ('ks@python.-yandex.ru', False),
            ('ks@python.yandex-.ru', False),
            ('ks@python.yandex.-ru', False),
            ('ks@python.yandex.ru-', False),
            ('ks@yandex!.ru', False),
            ('ks@yandex.morethanfour', False),
            ('ks@yande10.info', True),
            ('ks@yandex.5ru', False),
            ('ks@yandex.r-u', False),
            ('ks@yandex..ru', False),
            ('k' * 128 + '@ya.ru', True),
            ('s' * 129 + '@ya.ru', False),
            ('kiril15avelyev@ya.ru', True),
            ('kirill\savelyev@ya.ru', False),
            ('kirill_savelyev@ya.ru', True),
            ('kirill-savelyev@ya.ru', True),
            ('kirill.savelyev@ya.ru', True),
            ('kirill..savelyev@ya.ru', False),
            ('kirill"""savelyev@ya.ru', False),
            ('kirill"!,:"savelyev@ya.ru', True),
            ('kirill!",:"savelyev@ya.ru', False),
            ('kirill!,:savelyev@ya.ru', False))

    def testCheckMail(self):
        self.assertRaises(TypeError)
        for mail, value in self.mail_values:
            result = check_mail(mail)
            self.assertEqual(value, result)
            print(mail, '\t', check_mail(mail), '\t Test passed')


if __name__ == '__main__':
    unittest.main()
