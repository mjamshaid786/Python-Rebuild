# 10. Initials Generator: User se 3 words ka ek phrase input lein (e.g., "Hyper Text Markup"). Un teeno words ke pehle letters ko nikal kar uppercase mein acronym banayein (e.g., "HTM").

words = input("Enter 3 word's phrase:")

letter_1 = words[0]

space_1 = words.find(" ")
letter_2 = words[space_1 +1]

space_2 = words.find(" ", space_1 + 1)
letter_3 = words[space_2 + 1]

acronym = (letter_1 + letter_2 + letter_3).upper()
print(acronym)