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

# 1. Database Design and Integration

def test_menu_collection_exists():
    assert 'menu' in db.list_collection_names()

def test_orders_collection_exists():
    assert 'orders' in db.list_collection_names()

def test_menu_collection_structure():
    menu_fields = menu_collection.find_one().keys()
    expected_fields = {'dish_id', 'dish_name', 'dish_img', 'price', 'availability'}
    assert set(menu_fields) == expected_fields

def test_orders_collection_structure():
    order_fields = orders_collection.find_one().keys()
    expected_fields = {'customer_name', 'dishes', 'status'}
    assert set(order_fields) == expected_fields


# 2. Menu Mastery

def test_add_dish():
    dish = {
        'dish_id': 10,
        'dish_name': 'Pizza',
        'dish_img': 'pizza.jpg',
        'price': 10.99,
        'availability': True
    }
    response = app.test_client().post('/menu', json=dish)
    assert response.status_code == 200
    assert response.json == {'message': 'Dish added successfully'}

    # Verify that the dish is added to the menu collection
    menu_data = menu_collection.find_one({'dish_id': 1})
    assert menu_data['dish_name'] == 'Pizza'

    # Clean up by deleting the added dish
    menu_collection.delete_one({'dish_id': 1})

def test_update_availability():
    dish_id = 1
    updated_dish = {'availability': False}
    response = app.test_client().put(f'/menu/{dish_id}', json=updated_dish)
    assert response.status_code == 200
    assert response.json == {'message': 'Availability updated successfully'}

    # Verify that the dish availability is updated in the menu collection
    menu_data = menu_collection.find_one({'dish_id': 1})
    assert menu_data['availability'] == False


# 4. Taking Orders

def test_place_order():
    order = {
        'customer_name': 'John Doe',
        'dishes': [
            {'dish_id': 1, 'quantity': 2},
            {'dish_id': 2, 'quantity': 1}
        ],
        'status': 'received'
    }
    response = app.test_client().post('/order', json=order)
    assert response.status_code == 200
    assert response.json == {'message': 'Order placed successfully'}

    # Verify that the order is added to the orders collection
    order_data = orders_collection.find_one({'customer_name': 'John Doe'})
    assert order_data['dishes'][0]['dish_id'] == 1
    assert order_data['status'] == 'received'

    # Clean up by deleting the added order
    orders_collection.delete_one({'customer_name': 'John Doe'})

def test_change_order_status():
    customer_name = 'John Doe'
    updated_status = {'status': 'in progress'}
    response = app.test_client().put(f'/order/{customer_name}/status', json=updated_status)
    assert response.status_code == 200
    assert response.json == {'message': 'Order status updated successfully'}

    # Verify that the order status is updated in the orders collection
    order_data = orders_collection.find_one({'customer_name': 'John Doe'})
    assert order_data['status'] == 'in progress'


# invalid input

def test_add_dish_invalid_input():
    # Add a dish with missing required fields
    dish = {
        'dish_name': 'Pizza',
        'dish_img': 'pizza.jpg',
        'price': 10.99
        # 'availability' field is missing
    }
    response = app.test_client().post('/menu', json=dish)
    assert response.status_code == 400
    assert response.json == {'error': 'Invalid input'}

def test_update_availability_invalid_input():
    # Try to update dish availability with an invalid dish_id
    dish_id = 999
    updated_dish = {'availability': False}
    response = app.test_client().put(f'/menu/{dish_id}', json=updated_dish)
    assert response.status_code == 404
    assert response.json == {'error': 'Dish not found'}


# 6. Edge Case Excellence

def test_edge_cases():
    # Add a dish with a very long dish_name
    dish = {
        'dish_id': 1,
        'dish_name': 'X' * 1000,  # dish_name with 1000 characters
        'dish_img': 'pizza.jpg',
        'price': 10.99,
        'availability': True
    }
    response = app.test_client().post('/menu', json=dish)
    assert response.status_code == 400
    assert response.json == {'error': 'Invalid input'}

    # Try to update dish availability with an invalid dish_id (negative value)
    dish_id = -1
    updated_dish = {'availability': False}
    response = app.test_client().put(f'/menu/{dish_id}', json=updated_dish)
    assert response.status_code == 400
    assert response.json == {'error': 'Invalid dish_id'}




if __name__ == '__main__':
    pytest.main()
