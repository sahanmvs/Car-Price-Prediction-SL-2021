import json
import pickle
import numpy as np

__cars = None
__body = None
__transmission = None
__fuel = None
__condition = None
__data_columns = None
__model = None

def get_predicted_price(car_model,condition,body,transmission,fuel,year,capacity,mileage):
    try:
        car_model_index = __data_columns.index(car_model.lower())
        condition_index = __data_columns.index(condition.lower())
        body_index = __data_columns.index(body.lower())
        trans_index = __data_columns.index(transmission.lower())
        fuel_index = __data_columns.index(fuel.lower())
    except:
        car_model_index = -1
        condition_index = -1
        body_index = -1
        trans_index = -1
        fuel_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = year
    x[1] = capacity
    x[2] = mileage
    if car_model_index > 0:
        x[car_model_index] = 1
    if condition_index > 0:
        x[condition_index] = 1
    if body_index > 0:
        x[body_index] = 1
    if trans_index > 0:
        x[trans_index] = 1
    if fuel_index > 0:
        x[fuel_index] = 1

    return round(__model.predict([x])[0]/100000, 2)

def get_car_names():
    return __cars

def get_car_body():
    return __body

def get_car_transmission():
    return __transmission

def get_car_fuel():
    return __fuel

def get_car_condition():
    return __condition

def load_saved_artifacts():
    print("loading artifacts......start")
    global __data_columns
    global __cars
    global __body
    global __fuel
    global __condition
    global __transmission
    global __model

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __cars = __data_columns[3:290]
        __condition = __data_columns[290:293]
        __body = __data_columns[293:300]
        __transmission = __data_columns[300:303]
        __fuel = __data_columns[303:]

    with open("./artifacts/SL_car_price_prediction_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("loading artifacts......done")


if __name__ == "__main__":
    load_saved_artifacts()
    print(get_car_names())
    print(get_car_body())
    print(get_car_transmission())
    print(get_car_fuel())
    print()
    print(get_predicted_price('Toyota CHR','New','SUV','Automatic','Hybrid',2021,1200,0))
    print(get_predicted_price('Toyota Corolla', 'New', 'SUV', 'Automatic', 'Hybrid', 2021, 1200, 0))