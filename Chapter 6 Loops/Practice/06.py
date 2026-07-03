# Task 6 — Network Payload String Reverser
#	Scenario: Reversing data packets or strings for cryptographic operations.
#	Task: Take a string input and use a loop to construct and print the string completely in reverse order without using built-in slicing tools like [::-1].


data = input("Enter Payload OR any string: ")
l = len(data)
while l > 0:
    print(data[l-1])
    l -= 1

