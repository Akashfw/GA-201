from flask import Flask, jsonify, request
from pymongo import MongoClient
from flask_cors import CORS
from dotenv import load_dotenv
import os
# Load environment variables from the .env file
load_dotenv()

# Initialize Flask app and MongoDB client
app = Flask(__name__)
CORS(app)
client = MongoClient(os.getenv('MONGODB_URI'))
db = client['zesty_zomato']
menu_collection = db['menu']
orders_collection = db['orders']


menu_schema = {
    "dish_id": int,
    'dish_name': str,
    'dish_img':str,
    'price': float,
    'availability': bool
}

order_schema = {
    'customer_name': str,
    'dishes': [{
        'dish_id': int,
        'quantity': int
    }],
    'status': str
}


@app.route('/menu', methods=['GET'])
def get_menu():
    menu_data = menu_collection.find({}, {'_id': 0})
    return jsonify(list(menu_data))

@app.route('/menu', methods=['POST'])
def add_dish():
    dish = request.json
    menu_collection.insert_one(dish)
    return jsonify({'message': 'Dish added successfully'})

@app.route('/menu/<dish_id>', methods=['PUT'])
def update_availability(dish_id):
    dish = request.json
    menu_collection.update_one({'dish_id': dish_id}, {'$set': dish})
    return jsonify({'message': 'Availability updated successfully'})

@app.route('/menu/<dish_id>', methods=['DELETE'])
def delete_dish(dish_id):
    menu_collection.delete_one({'dish_id': dish_id})
    return jsonify({'message': 'Dish deleted successfully'})

@app.route('/order', methods=['POST'])
def place_order():
    order = request.json
    populated_order = []

    for item in order['dishes']:
        dish_id = item['dish_id']
        dish = menu_collection.find_one({'dish_id': dish_id}, {'_id': 0, 'dish_name': 1})
        item['dish_name'] = dish['dish_name']
        populated_order.append(item)

    order['dishes'] = populated_order
    orders_collection.insert_one(order)
    return jsonify({'message': 'Order placed successfully'})

@app.route('/order/<customer_name>/status', methods=['PUT'])
def change_order_status(customer_name):
    status = request.json['status']
    orders_collection.update_one({'customer_name': customer_name}, {'$set': {'status': status}})
    return jsonify({'message': 'Order status updated successfully'})

@app.route('/order/<customer_name>', methods=['GET'])
def get_order_details(customer_name):
    order_data = orders_collection.find({'customer_name': customer_name}, {'_id': 0})
    populated_order_data = []

    for order in order_data:
        populated_order = []

        for item in order['dishes']:
            dish_id = item['dish_id']
            dish = menu_collection.find_one({'dish_id': dish_id}, {'_id': 0, 'dish_name': 1})
            item['dish_name'] = dish['dish_name']
            populated_order.append(item)

        order['dishes'] = populated_order
        populated_order_data.append(order)

    return jsonify(populated_order_data)


@app.route('/orders', methods=['GET'])
def get_all_orders():
    order_data = orders_collection.find({}, {'_id': 0})

    all_orders = []
    for order in order_data:
        customer_name = order['customer_name']
        dishes = []
        total_amount = 0

        for dish in order['dishes']:
            dish_id = dish['dish_id']
            dish_quantity = dish['quantity']
            dish_details = menu_collection.find_one({'dish_id': dish_id}, {'_id': 0, 'dish_name': 1, 'price': 1})
            dish_name = dish_details['dish_name']
            dish_price = dish_details['price']
            dish_amount = dish_quantity * dish_price
            total_amount += dish_amount

            dish_info = {
                'dish_name': dish_name,
                'quantity': dish_quantity,
                'amount': dish_amount
            }
            dishes.append(dish_info)

        order_info = {
            'customer_name': customer_name,
            'dishes': dishes,
            'total_amount': total_amount
        }
        all_orders.append(order_info)

    return jsonify(all_orders)


if __name__ == '__main__':
    app.run()




















