# remake of original microservice A using HTTP requests instead of text files
#
# Item Code Lookup microservice for Vending Machine Simulator
#
# This microservice receives an item code from vending machine,
# and returns the corresponding animation code

from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

item_to_animation = {
    'A1': '1',
    'A2': '2',
    'A3': '3',
    'B1': '4',
    'B2': '5',
    'B3': '6',
    'C1': '7',
    'C2': '8',
    'C3': '9',
}

@app.route('/get-item-code', methods=['POST'])
def get_item_code():
    # handles button selection from the vending machine
    data = request.json

    if not data or 'itemCode' not in data:
        return jsonify({"error": "need item code"})
    
    item_code = data['itemCode']
    animation_code = item_to_animation.get(item_code)

    return jsonify({"animation_code": animation_code})

if __name__ == '__main__':
    app.run(port=4291, debug=True)