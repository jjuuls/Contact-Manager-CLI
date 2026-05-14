"""
Contact Manager CLI

A command-line contact management application built with Python and SQLite.

Features:
- Add contacts
- View all contacts
- Search contacts
- Update contacts
- Delete contacts
- Persistent SQLite database storage
"""

import sqlite3


def connect():

    # Connect to the SQLite database
    conn = sqlite3.connect('contacts.db')
    
    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()
    
    # Create the contacts table if it does not already exist
    cursor.execute('''
    
                CREATE TABLE IF NOT EXISTS contacts (
            
                id INTEGER PRIMARY KEY AUTOINCREMENT,
            
                name TEXT NOT NULL,
            
                phone TEXT NOT NULL
        
                )
    
                ''')
    
    conn.commit() 

    return conn


def add_contact(name, phone):

    conn = connect()

    cursor = conn.cursor()

    # Check if a contact with the same name already exists (case-insensitive)
    cursor.execute('SELECT * FROM contacts WHERE LOWER(name) = LOWER(?)', (name,))

    existing_contact = cursor.fetchone() 

    if existing_contact:

        print('Contact already exists.')

        conn.close()

        return
    
    else:

        # Insert a new contact into the database
        cursor.execute('INSERT INTO contacts (name, phone) VALUES (?, ?)', (name, phone))

        conn.commit()

        print(f"Contact '{name}' added successfully.")

    conn.close()


def view_contacts():

    conn = connect()

    cursor = conn.cursor()

    # Fetch all contacts from the database
    cursor.execute('SELECT * FROM contacts')

    contacts = cursor.fetchall()

    # Check if the contacts table is empty
    if not contacts:

        print("No contacts found.")
    
        conn.close()

        return
    
    print("Contacts:")

    # Loop through and display each contact
    for contact in contacts:
    
        print(f"Name: {contact[1]}, Phone: {contact[2]}")

    conn.close()


def search_contact(name):
    
    conn = connect()

    cursor = conn.cursor()

    # Use LOWER() and LIKE for case-insensitive partial searching
    cursor.execute('SELECT * FROM contacts WHERE LOWER(name) LIKE ?', (f'%{name.lower()}%',))

    contacts = cursor.fetchall()

    if not contacts:

        print(f"No contacts found matching '{name}'.")

        conn.close()

        return

    print("Search Results:")

    # Display all matching contacts
    for contact in contacts:
    
        print(f"Name: {contact[1]}, Phone: {contact[2]}")

    conn.close()


def delete_contact(name):

    conn = connect()

    cursor = conn.cursor()

    # Delete a contact matching the provided name
    cursor.execute('DELETE FROM contacts WHERE LOWER(name) = ?', (name.lower(),))

    if cursor.rowcount == 0:

        print(f"No contact found with the name '{name}'.")

    else:

        print(f"Contact '{name}' deleted successfully.")

    conn.commit()

    conn.close()


def update_contact(name, new_phone):

    conn = connect()

    cursor = conn.cursor()

    # Update the phone number for a matching contact
    cursor.execute('UPDATE contacts SET phone = ? WHERE LOWER(name) = ?', (new_phone, name.lower()))

    if cursor.rowcount == 0:

        print(f"No contact found with the name '{name}'.")

    else:

        print(f"Contact '{name}' updated successfully.")

    conn.commit()

    conn.close()


def main():

    # Keep the application running until the user exits
    while True:
    
        print("\nContact Manager CLI")
    
        print("1. Add Contact")
    
        print("2. View Contacts")
    
        print("3. Search Contact")
    
        print("4. Delete Contact")
    
        print("5. Update Contact")
    
        print("6. Exit")
    
        choice = input("Enter your choice: ")

        if choice == '1':
    
            name = input("Enter contact name: ")
    
            phone = input("Enter contact phone number: ")
    
            add_contact(name, phone)
    
        elif choice == '2':
    
            view_contacts()
    
        elif choice == '3':
    
            name = input("Enter contact name to search: ")
    
            search_contact(name)
    
        elif choice == '4':
    
            name = input("Enter contact name to delete: ")
    
            delete_contact(name)

        elif choice == '5':

            name = input("Enter contact name to update: ")

            new_phone = input("Enter new phone number: ")

            update_contact(name, new_phone)

        elif choice == '6':
    
            print("Exiting Contact Manager. Goodbye!")
    
            break
    
        else:
    
            print("Invalid choice. Please try again.")


if __name__ == "__main__":

    main()
    