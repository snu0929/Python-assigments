# Step 2: User Interaction Euphoria

menu = {}          # Initialize an empty dictionary to store menu items
orders = []        # Initialize an empty list to store orders
order_id_counter = 1  # Initialize order ID counter

while True:
    print("\nMain Menu")
    print("1. Menu Management")
    print("2. Order Management")
    print("3. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        # Sub-menu for Menu Management
        while True:
            print("\nMenu Management")
            print("1. Show menu items")
            print("2. Add a new dish to the menu")
            print("3. Remove an existing dish from the menu")
            print("4. Go back to Main Menu")

            choice_menu = input("Enter your choice: ")
            if choice_menu == "1":
                # Logic to show menu items
                print("\nMenu Items:")
                for dish_id, dish_info in menu.items():
                    print(f"Dish ID: {dish_id}")
                    print(f"Name: {dish_info['name']}")
                    print(f"Price: {dish_info['price']}")
                    print(
                        f"Availability: {'Yes' if dish_info['availability'] else 'No'}")
                    print("-" * 20)

            elif choice_menu == "2":
                # Logic for adding a new dish
                dish_id = int(input("Enter dish ID: "))
                name = input("Enter dish name: ")
                price = float(input("Enter dish price: "))
                availability = input(
                    "Is the dish available? (yes/no): ").lower() == "yes"

                menu[dish_id] = {
                    "name": name,
                    "price": price,
                    "availability": availability
                }

                print(f"Dish '{name}' added to the menu.")
            elif choice_menu == "3":
                # Logic for removing an existing dish
                dish_id = int(input("Enter dish ID to remove: "))

                if dish_id in menu:
                    removed_dish = menu.pop(dish_id)
                    print(
                        f"Dish '{removed_dish['name']}' removed from the menu.")
                else:
                    print("Dish not found in the menu.")

            elif choice_menu == "4":
                print("Going back to Main Menu")
                break

            else:
                print("Invalid choice. Please enter a valid option.")
    elif choice == "2":
        # Sub-menu for Order Management
        while True:
            print("\nOrder Management")
            print("1. Take a new order")
            print("2. Update order status")
            print("3. Go back to Main Menu")

            choice_order = input("Enter your choice: ")
            if choice_order == "1":
                # Logic for taking a new order
                customer_name = input("Enter customer's name: ")
                dish_ids = input(
                    "Enter dish IDs (separated by spaces): ").split()

                order_valid = True  # Flag to check if the order is valid

                for dish_id in dish_ids:
                    dish_id = int(dish_id)

                    if dish_id not in menu:
                        print(
                            f"Dish with ID {dish_id} does not exist in the menu.")
                        order_valid = False
                        break

                    if not menu[dish_id]["availability"]:
                        print(
                            f"Dish '{menu[dish_id]['name']}' is not available.")
                        order_valid = False
                        break

                if order_valid:
                    order = {
                        "order_id": order_id_counter,
                        "customer_name": customer_name,
                        "dish_ids": [int(dish_id) for dish_id in dish_ids],
                        "status": "received"
                    }
                    orders.append(order)

                    print(
                        f"Order ID {order_id_counter} created for {customer_name}.")
                    order_id_counter += 1

                elif choice_order == "2":
                    # Logic for updating order status
                    order_id = int(input("Enter order ID to update status: "))
                    new_status = input("Enter new status for the order: ")

                    # Find the order in the orders list
                    found_order = None
                    for order in orders:
                        if order["order_id"] == order_id:
                            found_order = order
                            break

                    if found_order:
                        found_order["status"] = new_status
                        print(
                            f"Order ID {order_id} status updated to '{new_status}'.")
                    else:
                        print(f"Order ID {order_id} not found.")

                elif choice_order == "3":
                    # Logic for showing order status
                    order_id = int(input("Enter order ID to show status: "))

                    found_order = None
                    for order in orders:
                        if order["order_id"] == order_id:
                            found_order = order
                            break

                    if found_order:
                        print(f"Order ID: {order_id}")
                        print(f"Customer: {found_order['customer_name']}")
                        print(f"Status: {found_order['status']}")
                    else:
                        print(f"Order ID {order_id} not found.")
