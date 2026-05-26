# Login validation project
# Day 1 practice

# list of users registered in the cinema
approved_users = ["ana", "carlos", "maria", "elieser"]

# list of ticket registered to users 
approved_tickets = ["A123", "B456", "C789", "D321"]

# fuction that checks users and ticket security
def check_ticket(username, ticket_id):
    
    # this variable converts usernames from uppercase to lowercase
    username = username.lower()
    
    # this variable converts tickets from lowercase to uppercase
    ticket_id = ticket_id.upper()
    
    # this variable counts the ticket characters allowed
    ta = len(approved_tickets[0])
        
    # this variable counts the ticket characters sumitted
    tn = len(ticket_id)
    
    # if the username is in the list, it prints that the user can enter the cinema if not then prints the user is not registered.
    if username in approved_users:
        print("The user", username.upper(), "can enter the cinema")
    else: 
        print("The user", username.upper(), "is not registered.")
        return

    # this variable gets the user position number of the list 
    ind = approved_users.index(username)
       
        #if the ticket is not exactly 4 digits it prints that is an invalid ticket format
    if tn != ta:
        print("Invalid ticket format")
        return
        
    #if the tickets has the same position number that username it prints that is valid, if not, it prints that is not valid
    if ticket_id == approved_tickets[ind]:
        print("Ticket", ticket_id, "is valid for", username.upper())
    else:
        print("Ticket", ticket_id, "is NOT valid for", username.upper())
        
        
# after that, call the fuction with different values to test it 
check_ticket("Elieser", "d321")
check_ticket("Juan", "d321")
check_ticket("ana", "ab123")
check_ticket("CARLOS", "C789")
