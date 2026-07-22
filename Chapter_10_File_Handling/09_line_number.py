# print the line no...

def check_line_no ():
    find_line_no = input("Enter word for which you want to find line number: ")
    line_no = 1
    with open('practice.txt', 'r')as file:
        while True:
            data = file.readline()
            if (find_line_no in data):
                print(line_no)
                return
            line_no += 1
    return -1

print(check_line_no())