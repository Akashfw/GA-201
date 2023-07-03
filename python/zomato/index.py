import json

class Dish:
    def __init__(self, dish_id, dish_name, price, availability):
        self.dish_id = dish_id
        self.dish_name = dish_name
        self.price = price
        self.availability = availability

    def to_dict(self):
        return {
            'dish_id': self.dish_id,
            'dish_name': self.dish_name,
            'price': self.price,
            'availability': self.availability
        }

    @staticmethod
    def from_dict(data):
        dish_id = data['dish_id']
        dish_name = data['dish_name']
        price = data['price']
        availability = data['availability']
        return Dish(dish_id, dish_name, price, availability)

class Order:
    def __init__(self, order_id, customer_name, dishes, status='received'):
        self.order_id = order_id
        self.customer_name = customer_name
        self.dishes = dishes
        self.status = status

    def calculate_total_price(self):
        return sum(dish.price for dish in self.dishes)

    def to_dict(self):
        return {
            'order_id': self.order_id,
            'customer_name': self.customer_name,
            'dishes': [dish.__dict__ for dish in self.dishes],
            'status': self.status
        }

    @staticmethod
    def from_dict(data):
        order_id = data['order_id']
        customer_name = data['customer_name']
        dishes = [Dish.from_dict(dish_data) for dish_data in data['dishes']]
        status = data['status']
        return Order(order_id, customer_name, dishes, status)

class ZestyZomato:
    def __init__(self):
        self.menu = []
        self.orders = []
        self.order_counter = 1

    def add_dish(self, dish):
        self.menu.append(dish)
        print("New dish added to the menu.")

    def remove_dish(self, dish_id):
        for dish in self.menu:
            if dish.dish_id == dish_id:
                self.menu.remove(dish)
                print("Dish removed from the menu.")
                return
        print("Dish not found in the menu.")

    def update_availability(self, dish_id, availability):
        for dish in self.menu:
            if dish.dish_id == dish_id:
                dish.availability = availability
                print("Dish availability updated.")
                return
        print("Dish not found in the menu.")

    def view_menu(self):
        print("Menu:")
        for dish in self.menu:
            print(f"Dish ID: {dish.dish_id}, Name: {dish.dish_name}, Price: {dish.price}, Availability: {dish.availability}")

    def take_order(self, customer_name, dish_ids):
        dishes = []
        for dish_id in dish_ids:
            found = False
            for dish in self.menu:
                if dish.dish_id == dish_id and dish.availability == 'yes':
                    dishes.append(dish)
                    found = True
                    break
            if not found:
                print(f"Dish with ID {dish_id} is not available or does not exist. Order not processed.")
                return

        order = Order(self.order_counter, customer_name, dishes)
        self.orders.append(order)
        self.order_counter += 1
        print(f"New order (ID: {order.order_id}) received and added to the system.")

    def update_order_status(self, order_id, new_status):
        for order in self.orders:
            if order.order_id == order_id:
                order.status = new_status
                print(f"Order (ID: {order.order_id}) status updated: {new_status}")
                return
        print("Order not found.")

    def review_orders(self, status=None):
        print("All Orders:")
        for order in self.orders:
            if status is None or order.status.lower() == status.lower():
                print(f"Order ID: {order.order_id}, Customer: {order.customer_name}, Status: {order.status}")

    def calculate_total_price(self):
        total_price = sum(order.calculate_total_price() for order in self.orders)
        print(f"Total price of all orders: {total_price}")

    def save_data(self, menu_file, orders_file):
        menu_data = [dish.to_dict() for dish in self.menu]
        with open(menu_file, 'w') as f:
            json.dump(menu_data, f, indent=4)
        print("Menu data saved.")

        orders_data = [order.to_dict() for order in self.orders]
        with open(orders_file, 'w') as f:
            json.dump(orders_data, f, indent=4)
        print("Orders data saved.")

    def load_data(self, menu_file, orders_file):
        try:
            with open(menu_file, 'r') as f:
                menu_data = json.load(f)
                self.menu = [Dish.from_dict(dish_data) for dish_data in menu_data]
            print("Menu data loaded.")

            with open(orders_file, 'r') as f:
                orders_data = json.load(f)
                self.orders = [Order.from_dict(order_data) for order_data in orders_data]
                self.order_counter = max(order.order_id for order in self.orders) + 1
            print("Orders data loaded.")
        except FileNotFoundError:
            print("Data files not found. Starting with an empty menu and no orders.")


def display_options():
    print("********** Zesty Zomato Menu **********")
    print("1. Add a dish to the menu")
    print("2. Remove a dish from the menu")
    print("3. Update dish availability")
    print("4. View the menu")
    print("5. Take a new order")
    print("6. Update order status")
    print("7. Review all orders")
    print("8. Calculate the total price of all orders")
    print("9. Save dish and order data")
    print("10. Load dish and order data")
    print("11. Exit")


def main():
    zomato = ZestyZomato()
    menu_file = 'menu.json'
    orders_file = 'orders.json'
    zomato.load_data(menu_file, orders_file)

    while True:
        display_options()
        choice = input("Enter your choice (1-11): ")

        if choice == '1':
            dish_id = int(input("Enter dish ID: "))
            dish_name = input("Enter dish name: ")
            price = float(input("Enter price: "))
            availability = input("Enter availability (yes/no): ")
            dish = Dish(dish_id, dish_name, price, availability)
            zomato.add_dish(dish)

        elif choice == '2':
            dish_id = int(input("Enter dish ID to remove: "))
            zomato.remove_dish(dish_id)

        elif choice == '3':
            dish_id = int(input("Enter dish ID to update availability: "))
            availability = input("Enter new availability (yes/no): ")
            zomato.update_availability(dish_id, availability)

        elif choice == '4':
            zomato.view_menu()

        elif choice == '5':
            customer_name = input("Enter customer name: ")
            dish_ids = [int(x) for x in input("Enter dish IDs (separated by commas): ").split(',')]
            zomato.take_order(customer_name, dish_ids)

        elif choice == '6':
            order_id = int(input("Enter order ID to update status: "))
            new_status = input("Enter new status: ")
            zomato.update_order_status(order_id, new_status)

        elif choice == '7':
            status = input("Enter status to filter orders (leave blank to show all orders): ")
            zomato.review_orders(status)

        elif choice == '8':
            zomato.calculate_total_price()

        elif choice == '9':
            zomato.save_data(menu_file, orders_file)

        elif choice == '10':
            zomato.load_data(menu_file, orders_file)

        elif choice == '11':
            break

        else:
            print("Invalid choice. Please try again.")

        print()

    print("Exiting Zesty Zomato app.")
    zomato.save_data(menu_file, orders_file)


if __name__ == '__main__':
    main()
