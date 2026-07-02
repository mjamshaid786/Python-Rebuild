email = input("Enter your email: ")

# 1. Ensure the email is not empty and within the character limit
if 0 < len(email) <= 254:
    
    # 2. Check all remaining structural rules
    if (
        "@" in email and 
        "." in email and 
        email.count("@") == 1 and
        email.endswith((".com", ".org", ".net")) and
        email[0].isalnum() and 
        email[-1].isalnum()
    ):
        print("Done")
    else: 
        print("Check Again !")
else:
    print("Check Again !")