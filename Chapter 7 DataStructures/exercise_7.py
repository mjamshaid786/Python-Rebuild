'''
Exercise 2: Write a program that categorizes each mail message by which day of the week the 
commit was done. To do this look for lines that start with “From”, then look for the third word and 
keep a running count of each of the days of the week. At the end of the program print out the 
contents of your dictionary (order does not matter). 

'''
count = {}
filename = r"E:\Python Specialization  By Michigan University\Python_Specialization\Files\mbox-short.txt"
with open(filename, 'r') as file :
    for line in file :
        if line.startswith("From ") :
            words = line.split()
            day = words[2]
            count[day] = count.get(day, 0) +1
print(count)








