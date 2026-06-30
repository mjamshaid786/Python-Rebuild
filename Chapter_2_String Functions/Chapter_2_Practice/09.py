# 9. Character Counter: User se ek lamba sentence input lein aur phir ek single character input lein. Batayein ke wo character us sentence mein kitni baar aaya hai.

sentence = input("Enter a sentence: ").lower()
charachter = input("Enter a character to know the number of times a character appears in the sentence: ").lower()

print(f"{charachter}, appears {sentence.count(charachter)} times.")