import pickle
from flask import Flask, jsonify, request

app = Flask(__name__)

# Load menu data from menu.pkl
def load_menu_data():
    try:
        with open('menu.pkl', 'rb') as file:
            menu_data = pickle.load(file)
    except FileNotFoundError:
        menu_data = {}
    return menu_data

# Save menu data to menu.pkl
def save_menu_data(menu_data):
    with open('menu.pkl', 'wb') as file:
        pickle.dump(menu_data, file)

# Load order data from orders.pkl
def load_order_data():
    try:
        with open('orders.pkl', 'rb') as file:
            order_data = pickle.load(file)
    except FileNotFoundError:
        order_data = []
    return order_data

# Save order data to orders.pkl
def save_order_data(order_data):
    with open('orders.pkl', 'wb') as file:
        pickle.dump(order_data, file)

# Route to get all dishes from the menu
@app.route('/menu', methods=['GET'])
def get_menu():
    menu_data = load_menu_data()
    return jsonify(menu_data)

# Route to add a dish to the menu
@app.route('/menu', methods=['POST'])
def add_dish():
    dish = request.json
    menu_data = load_menu_data()
    dish_id = str(len(menu_data) + 1)
    menu_data[dish_id] = dish
    save_menu_data(menu_data)
    return jsonify({'message': 'Dish added successfully'})

# Route to edit the availability of a dish
@app.route('/menu/<dish_id>', methods=['PUT'])
def update_availability(dish_id):
    dish = request.json
    menu_data = load_menu_data()
    if dish_id in menu_data:
        menu_data[dish_id]['availability'] = dish['availability']
        save_menu_data(menu_data)
        return jsonify({'message': 'Availability updated successfully'})
    else:
        return jsonify({'error': 'Dish not found'})

# Route to delete a dish from the menu
@app.route('/menu/<dish_id>', methods=['DELETE'])
def delete_dish(dish_id):
    menu_data = load_menu_data()
    if dish_id in menu_data:
        del menu_data[dish_id]
        save_menu_data(menu_data)
        return jsonify({'message': 'Dish deleted successfully'})
    else:
        return jsonify({'error': 'Dish not found'})

# Route to place an order
@app.route('/order', methods=['POST'])
def place_order():
    order = request.json
    order_data = load_order_data()
    order_data.append(order)
    save_order_data(order_data)
    return jsonify({'message': 'Order placed successfully'})

# Route to change the status of an order
@app.route('/order/<customer_name>/status', methods=['PUT'])
def change_order_status(customer_name):
    status = request.json['status']
    order_data = load_order_data()
    for order in order_data:
        if order['customer_name'] == customer_name:
            order['status'] = status
            save_order_data(order_data)
            return jsonify({'message': 'Order status updated successfully'})
    return jsonify({'error': 'Order not found'})

# Route to retrieve order details by customer name
@app.route('/order/<customer_name>', methods=['GET'])
def get_order_details(customer_name):
    order_data = load_order_data()
    order_details = []
    for order in order_data:
        if order['customer_name'] == customer_name:
            order_details.append(order)
    return jsonify(order_details)

if __name__ == '__main__':
    app.run()
