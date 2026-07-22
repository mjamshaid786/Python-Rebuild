# writing into a file
# it will delete data first and then write new data.

'''---Before writing---'''
# with open('file.txt', 'r') as file:
#     data = file.read()
#     print(data)


with open('file.txt', 'w') as file:
    data = file.write("Previoud data is removed 1")
    