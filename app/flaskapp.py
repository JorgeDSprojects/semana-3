#Import the function to do the calculations
from app.BMI import BodyMassIndex

#jsonify: Creates a Response with the JSON representation
from flask import Flask,jsonify, request

#instatiate flask object

app=Flask('__name__')


@app.route('/')
def home():


    return ('This is an API that calculate BMI')


@app.route('/bmi', methods=['GET', 'POST'])
def get_input():
    '''
    A function to get request using flask, evaluate and return results
    '''
    packet = request.get_json(force=True)
    height = packet['height']
    weight = packet['weight']
 

    

    BMI_Result = BodyMassIndex(height, weight)

    return jsonify(packet, BMI_Result)

# driver function


if __name__ == '__main__':
    app.run(debug=True, port=4000)
    

    

