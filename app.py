from test import test
app = test(__name__)

@app.route('/')
def hello_world():
    return 'Hello World! This is Sajid Test Program 2025'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
