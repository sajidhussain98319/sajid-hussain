from flask import flask
app = flask(__name__)

@app.route('/')
def hello_world():
<<<<<<< HEAD
    return 'Hello World! This is networking'
=======
    return 'Hello World! This is Sajid networking'
>>>>>>> 6e7dfe6921bac6d85e07af8c207f3b15643a2a8d

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
