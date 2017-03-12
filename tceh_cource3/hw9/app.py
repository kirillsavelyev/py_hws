# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify, render_template


class Storage(object):
    obj = None

    users = None

    @classmethod
    def __new__(cls, *args):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
            cls.users = []
        return cls.obj

    def add(self, user):
        self.users.append(user)

    def get(self, index):
        return self.users[index]

    def rm(self, email, username):
        for user in self.users:
            if user.email == email and user.username == username:
                return self.users.remove(user)


class User(object):
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def to_json(self):
        return {
            'username': self.username,
            'email': self.email,
        }


app = Flask(__name__, template_folder='templates')

@app.route('/user/', methods=['GET', 'POST', 'DELETE'])
@app.route('/user', methods=['POST'])
def users_handler():
    storage = Storage()

    if request.method == 'POST':
        data = request.get_json()

        user = User(data['username'], data['email'])
        storage.add(user)

        return jsonify({'status': 'done'})
    elif request.method == 'GET':
        data = {storage.users.index(item): item.to_json() for item in storage.users}
        return jsonify(data)
    elif request.method == 'DELETE':
        data = request.get_json()
        storage.rm(data['email'], data['username'])

        return jsonify({'status': 'done'})


@app.route('/user/<int:index>/', methods=['GET'])
def user_by_id(index):
    storage = Storage()

    if request.method == 'GET':
        try:
            user = storage.users[index]
            data = {'username': user.username, 'email': user.email}

        except IndexError as ex:
            data = {'Error': str(ex)}

        return jsonify(data)


@app.route('/user/report/', methods=['GET'])
def users_report():
    storage = Storage()

    if request.method == 'GET':
        data = len(storage.users)

        return render_template('users_report.txt', data=data)


if __name__ == '__main__':
    app.run(host='localhost', port=4000)
