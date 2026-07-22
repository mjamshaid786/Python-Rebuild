'''
 Write a program to read through a mail log, build a histogram using a dictionary to 
count how many messages have come from each email address, and print the dictionary.
'''

count = {}
filename = r"E:\Python Specialization  By Michigan University\Python_Specialization\Files\mbox-short.txt"
with open(filename, 'r') as file :
    for line in file :
        if line.startswith("From ") :
            words = line.split()
            mail = words[1]
            count[mail] = count.get(mail, 0) +1

print(count)

