from config import *
from flask import Flask, render_template, request, redirect, url_for
from flask_babel import Babel
from database.database import DataBase

app = Flask(__name__)
app.config['DEBUG'] = app_debug
app.config['MY_PORT'] = my_port
app.config['MY_INTERNAL_IP'] = my_ip
babel = Babel(app)


@app.route('/')
def index():
    database = DataBase()
    return render_template('index.html', users=database.get_users(), columns=database.get_all_columns_of_table("user"))


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    database = DataBase()
    columns = database.get_all_columns_of_table("user")
    return render_template('register.html', inputs=columns)


@app.route('/register_user', methods=['POST', 'GET'])
def register_user():
    database = DataBase()
    database.register_user(request.form)
    return redirect(url_for('register'))

if __name__ == "__main__":
    app.run(host=app.config['MY_INTERNAL_IP'],
            port=app.config['MY_PORT'],
            debug=app.config['DEBUG'])
