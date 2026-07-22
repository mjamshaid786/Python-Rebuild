'''
Task:
Write a Python program that:

Asks the user to enter a sentence.

Counts how many times each character appears (excluding spaces).

Prints the character(s) that appear the most times.


'''

sentence = input("Enter a sentence :").upper()
sentence = sentence.split()
#print(sentence)
characters = {}
for word in sentence :
    for char in word :
        characters[char] = characters.get(char , 0) +1
    max_count = max(characters.values())

print("Most frequent word(s):")
for char, count in characters.items():
    if count == max_count:
        print(f"{char} : {count}")
    
