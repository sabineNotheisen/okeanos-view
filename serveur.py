from config import *
from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = app_debug
app.config['MY_PORT'] = my_port
app.config['MY_INTERNAL_IP'] = my_ip


@app.route('/login')
def index():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(host=app.config['MY_INTERNAL_IP'],
            port=app.config['MY_PORT'],
            debug=app.config['DEBUG'])
