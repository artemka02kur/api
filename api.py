from flask import Flask, jsonify, request, redirect, Response
import requests
# http://127.0.0.1:5000/get_weather_status?city=Minsk
app = Flask(__name__)
API_KEY = "a615d7244c398ed85ecfebcdd6452817"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


@app.route('/get_weather_status', methods=['GET'])
def get_weather_status():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "Параметр 'city' обязателен"}), 400

    if city == "info":
        return Response(status=100)

    if city == "redirect":
        return redirect("https://github.com", code=301)

    params = {
        'q': city,
        'appid': API_KEY
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return jsonify(weather_data), 200
    else:
        error_message = response.json().get(
            'message', 'Не удалось получить данные о погоде')
        return jsonify({"error": error_message}), response.status_code


if __name__ == '__main__':
    app.run(debug=True)