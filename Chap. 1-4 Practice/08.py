# Task 8 — Whitespace Cleaner Ask the user to type a word with extra spaces before and after it. Print the word before cleaning and after cleaning using .strip(). Also print the length of both versions to show the difference.

word = input("Enter a word with spaces before and after it: ")
print(f"Word before cleaning: {word} with length: {len(word)}")

print(f"Word after cleaning: {word.strip()} with length: {len(word.strip())}")
