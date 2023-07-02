import json

class Dish:
    def __init__(self, dish_id, dish_name, price, availability):
        self.dish_id = dish_id
        self.dish_name = dish_name
        self.price = price
        self.availability = availability

class Order:
    def __init__(self, order_id, customer_name, dishes):
        self.order_id = order_id
        self.customer_name = customer_name
        self.dishes = dishes
        self.status = 'received'

    def calculate_total_price(self):
        return sum(dish.price for dish in self.dishes)

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

    def calculate_total_price(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                total_price = order.calculate_total_price()
                print(f"Total price of Order ID {order_id}: {total_price}")
                return
        print("Order not found.")

    def save_data(self):
        data = {
            'menu': [dish.__dict__ for dish in self.menu],
            'orders': [order.__dict__ for order in self.orders],
            'order_counter': self.order_counter
        }
        with open('zesty_zomato_data.json', 'w') as file:
            json.dump(data, file)
        print("Data saved successfully.")

    def load_data(self):
        try:
            with open('zesty_zomato_data.json', 'r') as file:
                data = json.load(file)
                self.menu = [Dish(**dish_data) for dish_data in data['menu']]
                self.orders = [Order(**order_data) for order_data in data['orders']]
                self.order_counter = data['order_counter']
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("No previous data found.")

def print_menu():
    menu = """
    ----------------------------
    Zesty Zomato Menu Management
    ----------------------------
    1. Add a new dish to the menu
    2. Remove a dish from the menu
    3. Update dish availability
    4. Take a new order
    5. Update order status
    6. Review all orders
    7. Calculate total price of an order
    8. View orders with a specific status
    9. Save data
    10. Load data
    0. Exit
    ----------------------------
    """
    print(menu)


def main():
    zomato = ZestyZomato()
    zomato.load_data()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            dish_id = int(input("Enter dish ID: "))
            dish_name = input("Enter dish name: ")
            price = float(input("Enter dish price: "))
            availability = input("Enter dish availability (yes/no): ")
            dish = Dish(dish_id, dish_name, price, availability)
            zomato.add_dish(dish)

        elif choice == "2":
            dish_id = int(input("Enter dish ID to remove: "))
            zomato.remove_dish(dish_id)

        elif choice == "3":
            dish_id = int(input("Enter dish ID to update availability: "))
            availability = input("Enter new availability (yes/no): ")
            zomato.update_availability(dish_id, availability)

        elif choice == "4":
            customer_name = input("Enter customer name: ")
            dish_ids = [int(x) for x in input("Enter dish IDs (space-separated): ").split()]
            zomato.take_order(customer_name, dish_ids)

        elif choice == "5":
            order_id = int(input("Enter order ID to update status: "))
            new_status = input("Enter new status: ")
            zomato.update_order_status(order_id, new_status)

        elif choice == "6":
            zomato.review_orders()

        elif choice == "7":
            order_id = int(input("Enter order ID to calculate total price: "))
            zomato.calculate_total_price(order_id)

        elif choice == "8":
            status = input("Enter order status to filter (leave blank for all orders): ")
            zomato.review_orders(status)

        elif choice == "9":
            zomato.save_data()

        elif choice == "10":
            zomato.load_data()

        elif choice == "0":
            zomato.save_data()
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

        print()


if __name__ == "__main__":
    main()
