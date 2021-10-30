from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_car_names')
def get_car_names():
    response = jsonify({
        'cars': util.get_car_names()
    })
    response.headers.add('Access-control-Allow-Origin', '*')

    return response

@app.route('/get_car_body')
def get_car_body():
    response = jsonify({
        'body': util.get_car_body()
    })
    response.headers.add('Access-control-Allow-Origin', '*')

    return response

@app.route('/get_car_transmission')
def get_car_transmission():
    response = jsonify({
        'transmission': util.get_car_transmission()
    })
    response.headers.add('Access-control-Allow-Origin', '*')

    return response

@app.route('/get_car_fuel')
def get_car_fuel():
    response = jsonify({
        'fuel': util.get_car_fuel()
    })
    response.headers.add('Access-control-Allow-Origin', '*')

    return response

@app.route('/get_car_condition')
def get_car_condition():
    response = jsonify({
        'condition': util.get_car_condition()
    })
    response.headers.add('Access-control-Allow-Origin', '*')

    return response

@app.route('/predict_car_price', methods=['POST'])
def predict_car_price():
    car_model = request.form['cars']
    condition = request.form['condition']
    body = request.form['body']
    transmission = request.form['transmission']
    fuel = request.form['fuel']
    year = int(request.form['year'])
    capacity = float(request.form['capacity'])
    mileage = float(request.form['mileage'])

    response = jsonify({
        'estimated_price': util.get_predicted_price(car_model,condition,body,transmission,fuel,year,capacity,mileage)
    })
    response.headers.add('Access-control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask server for Car price prediction")
    util.load_saved_artifacts()
    app.run()