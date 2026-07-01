# Task 13 — Quote Formatter Ask the user for a quote and the author's name. Print it in this format: "YOUR QUOTE" — Author Name The quote should be in UPPERCASE and the author in title case.

quote = input("Enter any quote: ").upper()
author = input("Enter author's name: ").title()

print(f"\"{quote}\" | {author}")