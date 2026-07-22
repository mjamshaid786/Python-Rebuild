'''
Task:
Write a Python program that:
Asks the user to enter a sentence.
Counts how many times each word appears.
Then prints the word(s) that appear the most times (i.e., with the highest frequency).
'''

sentence = input("Enter a sentence :")
sentence = sentence.split()

words = {}

for word in sentence :
    words[word] = words.get(word, 0) +1
max_count = max(words.values())

# Step 3: Print words with the highest frequency
print("Most frequent word(s):")
for word, count in words.items():
    if count == max_count:
        print(f"{word} : {count}")
