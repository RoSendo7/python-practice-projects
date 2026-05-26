# User Authentication System
# Day 2 practice

# list of users registered in the system
approved_users = ["ana", "carlos", "maria", "elieser", "carla", "sophia"]

# list of user passwords 
passwords = ["apples1", "banana2", "orange3", "python4", "pears5", "olives6"]

# store attempts globally
attempts = 0

# fuction that validates user login
def login(username, password):
    
    # convert inputs to lowercase 
    username = username.lower()
    password = password.lower()
    
    # access global attempts variable
    global attempts
    
    # validate user existence, password length, and attempts.
    if username not in approved_users:
        print(f"The user {username} does not exists!")
    elif len(password) < 6:
        print("Password too short.")
        attempts += 1
        print(f"Attempts:", attempts)
        return
    elif attempts >= 3:
        print("Account locked.")
        return
    # if login data is valid, verify the password
    else:
        unum = approved_users.index(username)
        if password == passwords[unum]:
            print(f"Welcome {username}!")
            attempts = 0
        else:
            print(f"Wrong password or username.")
            attempts += 1
            print(f"Attempts:", attempts)
            return attempts
            
# test the function with different inputs.
login("maria", "apples1")
login("ELIESER", "python4")
login("ELIESER", "banana2")
login("ELIESER", "banan")
login("ELIESER", "banana231")
login("ELIESER", "banana12")
login("ELIESER", "banana231")
login("juan", "orange3")
