# Task 4 — Password Vowel & Symbol Counter
#	Scenario: Analyzing a user's chosen password to check character distribution.
#	Task: Loop through a user-provided string (password) and count exactly how many vowels (a, e, i, o, u) it contains.


password = input("Enter password:").lower()
vowels_count = 0
vowels = "a, e, i, o, u"
for v in password:
    if v in vowels:
        print(v)
        vowels_count += 1
print(f"There are {vowels_count} vowels in your password.")
