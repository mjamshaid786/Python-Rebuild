names = [['Ali', 80],
         ['Hassan', 78],
         ['Ahmad', 99]]

print(list(filter(lambda row: row[0].startswith('A'), names)))