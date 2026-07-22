'''
Task:
Create a dictionary where keys are names and values are phone numbers.
Write a function called lookup_number(name) that:
Takes a name as input
Returns the phone number if the name exists
Otherwise returns "Not Found"
'''

PhoneBook = {
    "ALI": "03001234567",
    "SARA": "03111234567"
}

def lookup_number(name) :
    if name in PhoneBook :
        return PhoneBook[name]
    else :
        return "Not found !"

name = input("Enter name to lookup number :").upper()
results =lookup_number(name)
print(results)