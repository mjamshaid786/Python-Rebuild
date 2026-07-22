'''
Write a program that asks the user to enter a full sentence.
Then count how many times each word appears in that sentence using a dictionary.
'''
words = {}
sentence = input("Enter a sentence :")
sentence = sentence.split()

for word in sentence :
    words[word] = words.get(word, 0) +1 

print(words)