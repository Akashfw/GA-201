weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}

def get_weather(city):
    return weather_data.get(city, {})

def add_weather(city, temperature, weather):
    weather_data[city] = {'temperature': temperature, 'weather': weather}
    return {'message': 'Weather data added successfully.'}

def update_weather(city, temperature=None, weather=None):
    if city in weather_data:
        if temperature is not None:
            weather_data[city]['temperature'] = temperature
        if weather is not None:
            weather_data[city]['weather'] = weather
        return {'message': 'Weather data updated successfully.'}
    return {'error': 'City not found.'}

def delete_weather(city):
    if city in weather_data:
        del weather_data[city]
        return {'message': 'Weather data deleted successfully.'}
    return {'error': 'City not found.'}
