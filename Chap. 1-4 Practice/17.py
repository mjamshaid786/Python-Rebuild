# Task 17 — Palindrome Check Ask the user to enter a word. Print the result of comparing the word to its reverse using ==. This will print True if it is a palindrome and False if not.

word = input("Enter any word: ").lower()
reverse = word[::-1]

print(word == reverse)