from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Channy :D'

@app.route('/sensor-data', methods=['POST'])
def sensor_data():
    data = request.get_json()
    temperature = data.get('temperature')
    humidity = data.get('humidity')

    # Process the data (for example, save to a database)
    print(f"Received temperature: {temperature}°C, humidity: {humidity}%")

    response = {
        "message": "Data received successfully",
        "temperature": temperature,
        "humidity": humidity
    }

    print(f"Sending response: {response}")

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)