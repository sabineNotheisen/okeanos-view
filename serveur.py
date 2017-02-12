from config import *
from flask import Flask, render_template, request
from flask.ext.babel import Babel

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
    inputs = [['name', 'text'], ['forename', 'text']]
    return render_template('register.html', inputs=inputs)

if __name__ == "__main__":
    app.run(host=app.config['MY_INTERNAL_IP'],
            port=app.config['MY_PORT'],
            debug=app.config['DEBUG'])
