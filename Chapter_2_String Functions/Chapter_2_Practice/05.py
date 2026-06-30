# 5.Shouting Chatbot: User se ek sentence input lein. Uske start aur end ki extra spaces khatam karein, saare spaces ko triple underscore (___) se replace karein, aur poore sentence ko uppercase mein convert karke print karein.

sentence = input("Enter any sentece: ")

print(sentence.strip().replace(" ", "---").upper())