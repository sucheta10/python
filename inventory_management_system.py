# Inventory Management System
# Create a Python application that helps a small business manage its inventory. The inventory data should be stored in a dictionary with the item name as the key and a list as the value containing the quantity and price per unit, like this: {item_name: [quantity, price_per_unit]}. Your program should be able to add new items, update existing items, remove items, and display the entire inventory. Additionally, the inventory should be loaded from and saved to a file using JSON format.

import json
def load_inventory(file_name):
    try:
        with open(file_name, 'r') as file:
            inventory = json.load(file)
    except FileNotFoundError:
        inventory = {}
    return inventory

def save_inventory(inventory, file_name):
    with open(file_name, 'w') as file:
        json.dump(inventory, file, indent=4)

def add_item(inventory, item_name, quantity, price_per_unit):
    if item_name in inventory:
        print("Item already exists in inventory. Use 'update' to change quantity or price.")
    else:
        inventory[item_name] = [quantity, price_per_unit]
        print(item_name,"added to inventory.")

def update_item(inventory, item_name, quantity, price_per_unit):
    if item_name in inventory:
        inventory[item_name] = [quantity, price_per_unit]
        print(item_name,"updated in inventory.")
    else:
        print("Item does not exist in inventory. Use 'add' to add a new item.")

def remove_item(inventory, item_name):
    if item_name in inventory:
        del inventory[item_name]
        print(item_name, "removed from inventory.")
    else:
        print("Item does not exist in inventory.")

def display_inventory(inventory):
    if inventory:
        print("Current Inventory:")
        for item, details in inventory.items():
            print(f"Item: {item}, Quantity: {details[0]}, Price per Unit: ${details[1]}")
    else:
        print("Inventory is empty.")

def main():
    inventory_file = 'inventory.json'
    inventory = load_inventory(inventory_file)

    while True:
        print("\nMenu:")
        print("1. Add new item")
        print("2. Update existing item")
        print("3. Remove item")
        print("4. Display inventory")
        print("5. Save and Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price_per_unit = float(input("Enter price per unit: "))
            add_item(inventory, item_name, quantity, price_per_unit)
        elif choice == '2':
            item_name = input("Enter item name to update: ")
            quantity = int(input("Enter new quantity: "))
            price_per_unit = float(input("Enter new price per unit: "))
            update_item(inventory, item_name, quantity, price_per_unit)
        elif choice == '3':
            item_name = input("Enter item name to remove: ")
            remove_item(inventory, item_name)
        elif choice == '4':
            display_inventory(inventory)
        elif choice == '5':
            save_inventory(inventory, inventory_file)
            print("Inventory saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()
