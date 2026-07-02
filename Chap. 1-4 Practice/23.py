# Task 23 — Middle Character Finder Ask the user to enter a word with an odd number of characters. Calculate the middle index using len(word) // 2 and print the character at that position using indexing.

word = input("Enter a word with odd number of characters: ")
mid = len(word) // 2

print(mid)
print(word[mid])