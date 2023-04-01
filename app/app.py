from flask import Flask

from src.places.place import Place

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/get-place')
def get_place():
    place = Place(37.79304000016842, -122.41853845767118)
    return place.get_location()

if __name__ == '__main__':
    app.run(debug=True)