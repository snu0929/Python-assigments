# canteen.py

# Define an empty dictionary to store the snack inventory
snack_inventory = {}

# Variable to keep track of the total number of snacks sold
total_snacks_sold = 0


def add_snack():
    try:
        snack_id = int(input("Enter the snack ID: "))
        name = input("Enter the snack name: ")
        price = float(input("Enter the snack price: "))
        stocks_available = int(input("Enter the number of stocks available: "))

        # Validate price and stocks_available
        if price <= 0:
            raise ValueError("Price must be a positive number.")
        if stocks_available < 0:
            raise ValueError(
                "Stocks available must be a non-negative integer.")

        snack_details = {
            "name": name,
            "price": price,
            # Check if stocks available for availability
            "availability": stocks_available > 0,
            "stocks_available": stocks_available  # Store the number of stocks available
        }

        snack_inventory[snack_id] = snack_details
        print(f"Snack with ID {snack_id} has been added to the inventory.")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def remove_snack():
    try:
        snack_id = int(input("Enter the snack ID to remove: "))
        if snack_id in snack_inventory:
            del snack_inventory[snack_id]
            print(
                f"Snack with ID {snack_id} has been removed from the inventory.")
        else:
            print(f"Snack with ID {snack_id} is not found in the inventory.")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def update_availability():
    try:
        snack_id = int(input("Enter the snack ID to update availability: "))
        if snack_id in snack_inventory:
            availability = input("Is the snack available? (yes/no): ").lower()
            snack_inventory[snack_id]["availability"] = availability == "yes"
            print(
                f"Availability of snack with ID {snack_id} has been updated.")
        else:
            print(f"Snack with ID {snack_id} is not found in the inventory.")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def display_inventory():
    if not snack_inventory:
        print("The inventory is currently empty.")
    else:
        print("Snack Inventory:")
        print("ID | Name | Price | Availability | Stocks Available")
        for snack_id, details in snack_inventory.items():
            availability = "Yes" if details["availability"] else "No"
            stocks_available = details["stocks_available"]
            print(
                f"{snack_id} | {details['name']} | {details['price']} | {availability} | {stocks_available}")

# Exercise 4: Implementing the Menu-Based Application


def display_menu():
    print("\nMenu:")
    print("1. Add Snack")
    print("2. Remove Snack")
    print("3. Update Snack Availability")
    print("4. Display Snack Inventory")
    print("5. Sell Snack")
    print("6. Display Total Snacks Sold")
    print("7. Display Low Stock Snacks")
    print("8. Update Snack Details")
    print("9. Reset Inventory")
    print("10. Exit")


def sell_snack():
    global total_snacks_sold
    snack_id = int(input("Enter the snack ID to sell: "))
    if snack_id in snack_inventory:
        snack = snack_inventory[snack_id]
        if snack["availability"]:
            print(f"Snack: {snack['name']} (ID: {snack_id})")
            print(f"Price: {snack['price']}")
            print(f"Available Stocks: {snack['stocks_available']}")

            try:
                num_to_sell = int(
                    input("Enter the number of stocks to sell: "))
                if num_to_sell <= 0:
                    raise ValueError(
                        "Number of stocks to sell must be a positive integer.")
                if num_to_sell > snack["stocks_available"]:
                    raise ValueError("Not enough stocks available to sell.")

                snack["stocks_available"] -= num_to_sell
                total_snacks_sold += num_to_sell
                print(
                    f"{num_to_sell} stocks of {snack['name']} (ID: {snack_id}) have been sold.")
            except ValueError as e:
                print(f"Invalid input: {e}")
        else:
            print("Sorry, the snack is currently out of stock.")
    else:
        print(f"Snack with ID {snack_id} is not found in the inventory.")


def display_total_sold():
    print(f"Total snacks sold: {total_snacks_sold}")


def display_low_stock_snacks():
    print("\nLow Stock Snacks:")
    low_stock_threshold = 5  # Adjust this threshold as needed
    low_stock_found = False
    for snack_id, details in snack_inventory.items():
        if details["availability"] and low_stock_threshold > 0:
            low_stock_found = True
            print(
                f"{details['name']} (ID: {snack_id}) - {low_stock_threshold} left in stock.")
            low_stock_threshold -= 1
    if not low_stock_found:
        print("No snacks running low in stock.")


def update_snack_details():
    try:
        snack_id = int(input("Enter the snack ID to update details: "))
        if snack_id in snack_inventory:
            print("Current Details:")
            print(f"Name: {snack_inventory[snack_id]['name']}")
            print(f"Price: {snack_inventory[snack_id]['price']}")
            print(
                f"Availability: {'Yes' if snack_inventory[snack_id]['availability'] else 'No'}")

            # Get updated details
            name = input("Enter updated snack name: ")
            price = float(input("Enter updated snack price: "))
            availability = input("Is the snack available? (yes/no): ").lower()

            # Validate price
            if price <= 0:
                raise ValueError("Price must be a positive number.")

            # Update details
            snack_inventory[snack_id]['name'] = name
            snack_inventory[snack_id]['price'] = price
            snack_inventory[snack_id]['availability'] = availability == "yes"
            print(f"Details for snack with ID {snack_id} have been updated.")
        else:
            print(f"Snack with ID {snack_id} is not found in the inventory.")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def reset_inventory():
    global total_snacks_sold
    snack_inventory.clear()
    total_snacks_sold = 0
    print("The inventory has been reset.")

# ... (remaining code)


# Exercise 5: Finalizing the Application
if __name__ == "__main__":
    while True:
        display_menu()
        try:
            # Update the range for choices
            choice = int(input("Enter your choice (1-10): "))
            if choice == 1:
                add_snack()
            elif choice == 2:
                remove_snack()
            elif choice == 3:
                update_availability()
            elif choice == 4:
                display_inventory()
            elif choice == 5:
                sell_snack()
            elif choice == 6:
                display_total_sold()
            elif choice == 7:
                display_low_stock_snacks()  # Option 7: Display Low Stock Snacks
            elif choice == 8:
                update_snack_details()  # Option 8: Update Snack Details
            elif choice == 9:
                reset_inventory()  # Option 9: Reset Inventory
            elif choice == 10:
                print("Goodbye! Have a great day!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError as e:
            print(f"Invalid input: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
