data = []

files  = [
    'report.csv',
    'data.xlsx',
    'summary.docx',
    'report.csv',
    'data.csv'
]
for file in files:
    if file not in  data:
        data.append(file)
        print("file Transfred")
    else:
        print("Duplicate File Located.", file)      

print(data)