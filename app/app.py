from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/get-places')
def get_places():
    return 'Places here!'

if __name__ == '__main__':
    app.run(debug=True)