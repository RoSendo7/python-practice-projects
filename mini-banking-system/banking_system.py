# Bank Transaction System
# Day 3 practice

# list of users registered in the system
users = ["elieser", "maria", "carlos", "ana", "julia", "gabriela", "laura"]

# list of user balances
balances = [1500, 3200, 500, 1800, 900, 2000, 2850]

# store transactions globally  
transactions = []

# bank function system
def bank(username, action, amount=0):
    
    # convert inputs to lowercase
    username = username.lower()
    action = action.lower()
    
    # check user existence, otherwise stop the function
    if username in users:
        print(f"Welcome back {username}!")
    else:
        print("User not found.")
        return
    
    # get the user's index position
    un = users.index(username)
    
    # deposit, withdraw, check balance, or show transactions
    if action == "deposit":
        # check for invalid deposit amount
        if amount <= 0:
            print("Invalid amount.")
        else:
            balances[un] += amount 
            print(f"you just deposited {amount}")
            print(f"Your new balance is {balances[un]}.")
            # store this action in transactions variable
            transactions.append(f"{username} deposited {amount}")    
    # action withdraw
    elif action == "withdraw":
        # check if balance is sufficient
        if amount > balances[un]:
            print("Insufficient founds.")
        else:
            balances[un] -= amount 
            print(f"you just withdrew {amount}")
            print(f"Your new balance is {balances[un]}.")
            # store this action in transactions variable
            transactions.append(f"{username} withdrew {amount}")
    # action check display current balance
    elif action == "check":
        print(f"Your balance {username} is {balances[un]}.") 
    # action transactions display transaction history
    elif action == "transactions":
        print("Transactions:")
        for transaction in transactions:
            print("-", transaction)
    
    
bank("elieser", "deposit", 800)
bank("elieser", "deposit", 0)
bank("elieser", "withdraw", 1000)
bank("elieser", "withdraw", 2000)
bank("juan", "check", 2000)
bank("elieser", "withdraw", 1000)
bank("elieser", "check")
