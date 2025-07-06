"""
Inventory Management System
- Add new items with price and quantity
- Update item quantities
- View all items
- Search for items
- Calculate total inventory value
- Save/Load data to/from file
"""

import json
import os

class Inventory:
    def __init__(self):
        self.items = {}
        self.load_data()
    
    def add_item(self, name, price, quantity):
        """Add new item to inventory"""
        if name in self.items:
            print(f"{name} already exists in inventory.")
            return False
        self.items[name] = {"price": float(price), "quantity": int(quantity)}
        self.save_data()
        print(f"Added {name} to inventory.")
        return True
    
    def update_item(self, name, quantity_change):
        """Update existing item quantity"""
        if name not in self.items:
            print(f"{name} not found in inventory.")
            return False
        self.items[name]["quantity"] += quantity_change
        if self.items[name]["quantity"] < 0:
            self.items[name]["quantity"] = 0
        self.save_data()
        print(f"Updated {name} quantity.")
        return True
    
    def view_inventory(self):
        """Display all inventory items"""
        print("\nCurrent Inventory:")
        print("-" * 40)
        print(f"{'Item':<20}{'Price':<10}{'Quantity':<10}")
        print("-" * 40)
        for name, details in self.items.items():
            print(f"{name:<20}${details['price']:<10}{details['quantity']:<10}")
        print("-" * 40)
        print(f"Total items: {len(self.items)}")
        print(f"Total value: ${self.calculate_total_value():.2f}")
    
    def search_item(self, name):
        """Search for specific item"""
        if name in self.items:
            print(f"\nItem found: {name}")
            print(f"Price: ${self.items[name]['price']}")
            print(f"Quantity: {self.items[name]['quantity']}")
        else:
            print(f"\n{name} not found in inventory.")
    
    def calculate_total_value(self):
        """Calculate total inventory value"""
        return sum(item['price'] * item['quantity'] for item in self.items.values())
    
    def save_data(self):
        """Save inventory to file"""
        with open("inventory.json", "w") as f:
            json.dump(self.items, f)
    
    def load_data(self):
        """Load inventory from file"""
        if os.path.exists("inventory.json"):
            with open("inventory.json", "r") as f:
                self.items = json.load(f)

def main():
    inventory = Inventory()
    
    while True:
        print("\nInventory Management System")
        print("1. Add new item")
        print("2. Update item quantity")
        print("3. View all items")
        print("4. Search for item")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            inventory.add_item(name, price, quantity)
        
        elif choice == "2":
            name = input("Enter item name: ")
            change = int(input("Enter quantity change (+/-): "))
            inventory.update_item(name, change)
        
        elif choice == "3":
            inventory.view_inventory()
        
        elif choice == "4":
            name = input("Enter item name to search: ")
            inventory.search_item(name)
        
        elif choice == "5":
            print("Exiting inventory system...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
