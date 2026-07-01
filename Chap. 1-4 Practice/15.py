# Task 15 — Keyword Finder Ask the user to enter a sentence and a keyword. Print True or False based on whether the keyword exists in the sentence using the in operator.

sentence = input("Enter a sentence: ").lower()
word = input("Enter a word you want to find: ").lower()

print (word in sentence)