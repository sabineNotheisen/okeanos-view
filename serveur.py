from config import *
from flask import Flask, render_template
from flask_babel import Babel
from database.database import DataBase

app = Flask(__name__)
app.config['DEBUG'] = app_debug
app.config['MY_PORT'] = my_port
app.config['MY_INTERNAL_IP'] = my_ip
babel = Babel(app)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    database = DataBase()
    columns = database.get_all_columns_of_table("user")
    return render_template('register.html', inputs=columns)

if __name__ == "__main__":
    app.run(host=app.config['MY_INTERNAL_IP'],
            port=app.config['MY_PORT'],
            debug=app.config['DEBUG'])
