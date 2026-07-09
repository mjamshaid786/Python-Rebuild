# Remove Duplicates: Remove duplicates from a list while maintaining the original order.
list = [1, 2, 3, 5, 6, 3, 7, 5]
cleaned = []

for c in list:
    if c not in cleaned:
        cleaned.append(c)
    else:
        print(c, "Already exitsts !")
print("-" * 20)
print("Duplicate removed !")
print(cleaned)