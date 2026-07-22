# searching data inside a file

with open('practice.txt', 'r') as file:
    data = file.read()
# print(data)
if data.find("lerrning") != -1: #find() return -1 if data is not found
    print("Found",)
else:
    print("Not Found")