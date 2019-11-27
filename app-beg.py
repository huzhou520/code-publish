from flask import Flask

app = Flask(__name__)

app.route('/index')
def index():
    return 'Index'

app.route('/index2')
def index2():
    return 'Index2'

app.route('/index3')
def index3():
    return 'Index3'


if __name__ == '__main__':
    app.run()