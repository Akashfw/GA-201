class Snack:
    def __init__(self, snack_id, snack_name, price, availability):
        self.snack_id = snack_id
        self.snack_name = snack_name
        self.price = price
        self.availability = availability

class Canteen:
    def __init__(self):
        self.inventory = []
        self.sales_record = []

    def add_snack(self, snack):
        self.inventory.append(snack)
        print("Snack added to inventory.")

    def remove_snack(self, snack_id):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                self.inventory.remove(snack)
                print("Snack removed from inventory.")
                return
        print("Snack not found in inventory.")

    def update_availability(self, snack_id, availability):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                snack.availability = availability
                print("Snack availability updated.")
                return
        print("Snack not found in inventory.")

    def sell_snack(self, snack_id):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                if snack.availability == "yes":
                    snack.availability = "no"
                    self.sales_record.append(snack)
                    print("Snack sold and inventory updated.")
                    return
                else:
                    print("Snack is currently unavailable.")
                    return
        print("Snack not found in inventory.")

    def display_inventory(self):
        print("Current Snack Inventory:")
        for snack in self.inventory:
            print(f"Snack ID: {snack.snack_id}, Name: {snack.snack_name}, Price: {snack.price}, Availability: {snack.availability}")

    def display_sales_record(self):
        print("Sales Record:")
        for snack in self.sales_record:
            print(f"Snack ID: {snack.snack_id}, Name: {snack.snack_name}, Price: {snack.price}")


def print_menu():
    menu = """
    ----------------------------
    Canteen Inventory Management
    ----------------------------
    1. Add a snack to inventory
    2. Remove a snack from inventory
    3. Update snack availability
    4. Sell a snack
    5. Display inventory
    6. Display sales record
    0. Exit
    ----------------------------
    """
    print(menu)


def main():
    canteen = Canteen()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            snack_id = int(input("Enter snack ID: "))
            snack_name = input("Enter snack name: ")
            price = float(input("Enter snack price: "))
            availability = input("Enter snack availability (yes/no): ")
            snack = Snack(snack_id, snack_name, price, availability)
            canteen.add_snack(snack)

        elif choice == "2":
            snack_id = int(input("Enter snack ID to remove: "))
            canteen.remove_snack(snack_id)

        elif choice == "3":
            snack_id = int(input("Enter snack ID to update availability: "))
            availability = input("Enter new availability (yes/no): ")
            canteen.update_availability(snack_id, availability)

        elif choice == "4":
            snack_id = int(input("Enter snack ID to sell: "))
            canteen.sell_snack(snack_id)

        elif choice == "5":
            canteen.display_inventory()

        elif choice == "6":
            canteen.display_sales_record()

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

        print()


if __name__ == "__main__":
    main()
