from flask import Flask

app = Flask(__name__)

app.route('/index')
def index():
    return 'Index'

app.route('/index2')
def index2():
    return 'Index2'


if __name__ == '__main__':
    app.run()