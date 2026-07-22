'''
 This program records the domain name (instead of the address) where the message 
was sent from instead of who the mail came from (i.e., the whole email address). At the end of 
the program, print out the contents of your dictionary.
'''


count = {}

filename = r"E:\Python Specialization  By Michigan University\Python_Specialization\Files\mbox-short.txt"
with open(filename, 'r') as file :
    for line in file :
        if line.startswith("From ") :
            words = line.split("@")
            #print(words)
            mail = words[1]
            email = mail.split()
            fmail = email[0]
            #print(email)
            count[fmail] = count.get(fmail, 0) +1
        max_count = max(count.values())

print(count)

#for fmail, mx in count.items():
    #if mx == max_count :
        #print(f"{fmail} : {mx}")