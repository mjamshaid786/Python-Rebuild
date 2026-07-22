'''
  Add code to the above program to figure out who has the most messages in the file. 
After all the data has been read and the dictionary has been created, look through the dictionary 
using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most 
messages and print how many messages the person has.
'''

count = {}

filename = r"E:\Python Specialization  By Michigan University\Python_Specialization\Files\mbox-short.txt"
with open(filename, 'r') as file :
    for line in file :
        if line.startswith("From ") :
            words = line.split()
            mail = words[1]
            count[mail] = count.get(mail, 0) +1
        max_count = max(count.values())

#print(count)

for mail, mx in count.items():
    if mx == max_count :
        print(f"{mail} : {mx}")
