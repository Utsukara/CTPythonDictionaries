
# Objective:
# This assignment is designed to test and enhance your Python programming skills, focusing on real-world applications in customer service data management. You will practice correcting code, organizing customer data, and implementing a feedback system using Python dictionaries.

# Task 1: Customer Service Ticket Tracker
# Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

# Problem Statement:
# Develop a program that:

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket.
# Display all tickets or filter by status.
# Initialize with some sample tickets and include functionality for additional ticket entry.
# Example ticket structure:

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def add_ticket ():
    customer_name = input("Please enter your name: ")
    issue = input(f"What is the problem you are having?\n")
    ticket_id = 'Ticket' + str(len(service_tickets) + 1).zfill(3)
    service_tickets[ticket_id] = {"Customer": customer_name, "Issue": issue, "Status": "open"}
    print(f"Added new ticket: {ticket_id}\n")

def change_status():
    ticket_id = input("Enter the name of the ticket you would like to change: ")
    if ticket_id in service_tickets:
        print(f"{ticket_id} is currently {service_tickets[ticket_id]["Status"]}")
        ticket_status = input("How would you like to change the status of the ticket: ")
        service_tickets[ticket_id]["Status"] = ticket_status
    else:
        print(f"Ticket not found.\n")

def display_tickets(status = None):
    for ticket_id, details in service_tickets.items():
        if status is None or details["Status"] == status:
            print(f"ID: {ticket_id}, Customer: {details['Customer']}, Issue: {details['Issue']}, Status: {details['Status']}")

add_ticket()
change_status()
display_tickets()