# Task 10 — Word Replacer Ask the user to enter a sentence, a word to find, and a replacement word. Print the updated sentence using .replace().

sentence = input("Enter a sentence: ")
find_word = input("Enter a word you want to find and replace: ")
replacement_word = input("Enter new word: ")

updated_sentence = sentence.replace(find_word, replacement_word)
print(updated_sentence)