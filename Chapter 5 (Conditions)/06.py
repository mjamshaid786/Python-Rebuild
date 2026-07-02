#Task 6 — Phishing Email & Spam Keyword Scanner
#	Scenario: A basic text filter scanning incoming emails for malicious triggers.
#	Input: A long string representing an email body.
#	Logic: Scan the text for the following suspicious keywords/phrases: "urgent", "verify password", "lottery", "free prize", "bank details".
#	Output: If 2 or more of these unique phrases are found in the email, print "High Risk: Phishing Email Detected!". Otherwise, print "Email is safe".


email_body = """
Subject: UGENT Notification!

Dear Customer, 
We found a security issue with your profile. You must verify password within 24 hours. 
On a good note, your account was selected for our global lottery promotion! 
To claim your free prize and transfer the funds, please reply with your bank details.
""".lower()

trigge_count = 0
if "urgent" in email_body:
    trigge_count += 1
if "verify password" in email_body:
    trigge_count += 1
if "lottery" in email_body:
    trigge_count += 1
if "free prize" in email_body:
    trigge_count += 1
if "bank details" in email_body:
    trigge_count += 1

print("-" * 30)
print("Scanning Complete !")
print("-" * 30)

if trigge_count >= 2:
    print("-" * 30)
    print(f"{trigge_count} Trigger counts found.")
    print("High Risk: Phishing Email Detected!")
    print("-" * 30)
else:
    print("Email is safe")