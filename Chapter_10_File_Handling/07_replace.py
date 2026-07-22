
# replacing words in a file...


# step_1. Read data from the file
with open('practice.txt', 'r') as file:
    data = file.read()

# step_2. Replacing the data
new_data = data.replace("Java", "Python")
print(new_data)

# step_3 writing new data to file again..
with open('practice.txt', 'w') as file:
    updated_file = file.write(new_data)
    print("File Saved...!")
