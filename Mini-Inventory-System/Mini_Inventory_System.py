# Mini Inventory System
# Day 5 practice

# List of products in storage
storage = ["apple", "pineapple", "pear", "plate", "glass", "grape", "lime", "lemon", "strawberry"]

# List of quantities for each product
quantities = [80, 50, 130, 55, 64, 250, 90, 70, 150]

# Store the history of actions
history = []

# Main function to manage the inventory
def store(item="", action="", amount=0):
    
    # Clean user input: remove extra spaces and convert to lowercase
    item = item.lower().strip()
    action = action.lower().strip()
    
    # Check if the action is empty
    if action == "":
        print("Invalid action.")
    
    # Add a new product or update an existing product
    elif action == "add":
        
        # Check if the amount is valid
        if amount <= 0:
            print("Invalid amount.")
            
        # If the item is not in storage, add it as a new product
        elif item not in storage:
            storage.append(item)
            quantities.append(amount)
            print(f"{amount} {item} have been added to the storage.")
            history.append(f"[ADD NEW] {amount} {item.upper()}")
            
        # If the item already exists, update its quantity
        else:
            un = storage.index(item)
            quantities[un] += amount
            print(f"You have added {amount} {item}.")
            history.append(f"[ADD STOCK] {amount} {item.upper()}")
        
    # Show all products and their quantities
    elif action == "show":
        print("There are:")
        for quantity, items in sorted(zip(storage, quantities)):
            print("-", quantity, items)
            
    # Remove a quantity from an existing product
    elif action == "remove":
        
        # Check if the user selected an item
        if item == "":
            print("You have to select a item")
            
        # Check if the amount is valid
        elif amount <= 0:
            print("Invalid quantity.")
            
        else:
            # Check if the item exists in storage
            if item not in storage:
                print("The item is not in the storage")
            else:
                # Get the item's index position
                un = storage.index(item)
                
                # Check if there is enough quantity to remove
                if amount > quantities[un]:
                    print("You can not delete more than there are")
                
                # Remove the amount from the item quantity
                else:
                    quantities[un] -= amount
                    print(f"You have deleted {amount} {item}")
                    history.append(f"[REMOVE] {amount} {item.upper()}")
                    
    # Show the action history
    elif action == "history":
        print("Here is your historial:")
        for i in history:
            print(i)
    
    # Handle invalid actions
    else:
        print("Invalid action.")
    
store("","", 200)                
store("pin","add", 200)
store("apple","add ", 0)
store("apple","add", 100)
store("","show", 100)
store("","remove")
store("apple","remove", 0)
store("house","remove", 100)
store("apple","remove", 1000)
store("apple","remove", 150)
store("","show")
store("","history")
store("","dance")
