# replace +49 (176) 123-4567 to clean phone numbers

number = "+49 (176) 123-4567"
print("Old Number:", number)

new_number = number.replace("+", "").replace(" ", "").replace("(", "").replace(")", "").replace("-", "")
print("New Number:", new_number)