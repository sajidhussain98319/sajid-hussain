from flask import flask
app = flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World! This is Sajid networking'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
