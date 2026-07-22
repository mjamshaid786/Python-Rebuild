'''
Create Phonebook Dictionary
Input: Names and phone numbers from user (like 3 entries)
Task: Store name as key and phone as value. Then print the whole dictionary.
'''

PhoneBook = {}

while True :
    user_input = input("Enter 1 to save new contact :")
    if user_input == "1":
        name = input("Enter name :").upper()
        nmbr = input("Enter phone number :")
        PhoneBook[name] = nmbr
    else :
        break
print(PhoneBook)
