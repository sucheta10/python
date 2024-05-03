# Contact List Search
# Suppose you have a file named contacts.json that stores contact information in JSON format where each contact is a dictionary with name, email, and phone. Write a Python program that loads this data into a dictionary and allows the user to search for contacts by name. The search should be case-insensitive and display all matching contacts along with their details.

import json

def load_contacts(file_name):
    with open(file_name, 'r') as file:
        contacts = json.load(file)
    return contacts

def contacts_search(contacts, search):
    matches = []
    search = search.lower()  # Convert search to lowercase for case-insensitive search
    for contact in contacts:
        if search in contact['name'].lower():  # Check if the search is contained within the contact's name
            matches.append(contact)
    return matches

def main():
    contacts = load_contacts('C:/Users/Sucheta/OneDrive/Desktop/python/python_basics/contacts.json')

    while True:
        search_contact = input("Enter the name you want to search for (or type 'exit' to quit): ")
        if search_contact.lower() == 'exit':
            break

        search_results = contacts_search(contacts, search_contact)
        if search_results:
            print("Matching contacts:")
            for contact in search_results:
                print(f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}")
        else:
            print("No matching contacts found.")


main()
