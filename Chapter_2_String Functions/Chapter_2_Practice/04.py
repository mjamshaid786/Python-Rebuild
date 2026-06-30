# 4.Domain Extractor: User se unka email address input lein (e.g., amjad@gmail.com). String methods use karte hue sirf domain name (gmail.com) extract karke print karein.

email = input("Enter your email: ")

#print(email.find("@"))
print("Domain is: ", email[email.find("@") +1:])