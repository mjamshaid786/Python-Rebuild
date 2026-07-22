'''
Write a Python program that reads 
a string from the user and counts how many
 times each word appears in it. Store the result in a dictionary and print it.
'''
word = input("Enter a sentence :")
words = word.split()
count = {}
for char in words :
    count[char] = count.get(char, 0) +1

print(count)
