
# Objective:
# The aim of this assignment is to deepen your knowledge and practical skills in handling complex data structures using Python. You will work on real-world inspired tasks that require advanced manipulation of dictionaries, nested collections, and implementing custom functions for specific data processing needs.

# Task 1: Hotel Room Booking Tracker
# Enhance your ability to work with nested collections by developing a system to track room bookings for a hotel.

# Problem Statement:
# Develop a program that:

# Manages room bookings, where each room has details such as booking status (booked/available) and customer name.
# Implement functions to:
# Book a room (mark as booked and assign to a customer).
# Check-out a customer (mark room as available and remove customer name).
# Display the status of all rooms.
# Start with this initial hotel room structure:

hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

def book_room(room_number, customer_name):
    if room_number in hotel_rooms and hotel_rooms[room_number]["status"] == "available":
        hotel_rooms[room_number] = {"status": "booked", "customer": customer_name}
    else:
        print(f"Room number {room_number} cannot be booked.")

def check_out(room_number):
    if room_number in hotel_rooms and hotel_rooms[room_number]["status"] == "booked":
        hotel_rooms[room_number] = {"status": "available", "customer": ""}
    elif room_number not in hotel_rooms:
        print(f"Room {room_number} does not exist.")
    else:
        print(f"Room {room_number} is available.")

def display_status():
    for room_number, details in hotel_rooms.items():
        status = details["status"]
        print(f"{room_number}: {status}")

#example useage

book_room("101", "Jane Dee")
check_out("102")
display_status()