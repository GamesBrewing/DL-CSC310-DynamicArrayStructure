import csv
from operator import attrgetter

#Create Contact object to store information from .csv file
class Contact:
    def __init__(self, first_name, last_name, street, city, state, zip_code, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email

    #Return this string when a contact is printed. Without this it will just print the memory location of the contact.
    def __str__(self):
        return (f"""
                Name: {self.last_name}, {self.first_name}
                Address: {self.street}, {self.city}, {self.state}, {self.zip_code}
                Phone number: {self.phone_number}
                Email: {self.email}
                """)

#Read information from .csv file.
def read_file (filename):
    contacts = []
    try: 
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                contact = Contact(
                    first_name=row[0],
                    last_name=row[1],
                    street=row[2],
                    city=row[3],
                    state=row[4],
                    zip_code=row[5],
                    phone_number=row[6],
                    email=row[7]

                )
                contacts.append(contact)
    except FileNotFoundError:
        print(f'The file {filename} does not exist')
        return []
    
    return contacts


#Allow user to remove specific contacts.
def remove_contacts(contacts):
    print (""" 
            Remote contacts based on criteria.
            1. First name
            2. Last name
            3. City
            4. State
            5. Zip code
            6. Phone number
            7. Email
             """)
    
    choice = input("Enter which criteria you need.")

    if choice == '1':
        criteria = 'first_name'
    elif choice == '2':
        criteria = 'last_name'
    elif choice == '3':
        criteria = 'city'
    elif choice == '4':
        criteria = 'state'
    elif choice == '5':
        criteria = 'zip_code'
    elif choice == '6':
        criteria = 'phone_number'
    elif choice == '7':
        criteria = 'email'
    else:
        print("Invalid choice.")
        return contacts
    
    value = input(f"Enter what you would like removed: ")
    contacts = [contact for contact in contacts if getattr(contact, criteria) != value]

    return contacts

def main():
    filename = "us-contacts.csv"
    contacts = read_file(filename)
    if contacts:
        contacts = sorted(contacts, key = attrgetter('last_name'))

        # # #Remove a last name based off a specific name
        # remove_by_last_name = "Brideau"
        # contacts = [contact for contact in contacts if contact.last_name !=remove_by_last_name]
        print("Would you like to remove specific contacts?")
        choice = input("Enter 1 for yes or 0 for no: ")
        if choice == 1:
            contacts = remove_contacts(contacts)

        
        print("Users data read from file:")
        for i in range(49, len(contacts), 50):
            print(contacts[i])

if __name__ == '__main__':
    main()