from flask import Flask, jsonify, request
from weather import get_weather, add_weather, update_weather, delete_weather

app = Flask(__name__)

@app.route('/weather/<string:city>')
def weather(city):
    weather_info = get_weather(city)
    return jsonify(weather_info)

@app.route('/weather', methods=['POST'])
def add_weather_route():
    data = request.get_json()
    city = data.get('city')
    temperature = data.get('temperature')
    weather = data.get('weather')

    if city and temperature and weather:
        response = add_weather(city, temperature, weather)
        return jsonify(response)
    else:
        return jsonify({'error': 'Invalid request body.'}), 400

@app.route('/weather/<string:city>', methods=['PUT'])
def update_weather_route(city):
    data = request.get_json()
    temperature = data.get('temperature')
    weather = data.get('weather')

    response = update_weather(city, temperature, weather)
    return jsonify(response)

@app.route('/weather/<string:city>', methods=['DELETE'])
def delete_weather_route(city):
    response = delete_weather(city)
    return jsonify(response)

if __name__ == '__main__':
    app.run()
