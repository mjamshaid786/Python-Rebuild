'''-----LIBRARY BOOK MANAGEMENT SYSTEM-----'''

'''-----Main Menu-----'''

books = [
    {
        'Title' : 'to kill a mockingbird',
        'Author' : 'Harper Lee',
        'Is_Available' : True 
    },
    {
        'Title' : '1984',
        'Author' : 'George Orwell',
        'Is_Available' : True
    },
    {
        'Title' : 'the great gatsby',
        'Author' : 'F. Scott Fitzgerald',
        'Is_Available' : False
    }
]

'''-----ADD BOOK-----'''
def add_book():
    new_book = {}
    title = input("Enter Title of Book: ").lower().startswith()
    author = input("Enter Author Name: ").lower().strip()
    available = True
    new_book.update({'Title': title, 'Author' : author, 'Is_Available' : available})
    books.append(new_book)
    print("Book Added To Library.")

'''-----DISPLAY ALL BOOK-----'''
def display_books():
    if len(books) == 0:
        print("Libray is empty")
    else:
        for book in books:
            print(book)

'''-----SEARCH A BOOK-----'''
def search_book():
    title = input("Enter Book Title: ").lower().strip()
    for book in books:
        if book['Title'] == title:
            print(book)
            break
        else:
            print("Not Found")

'''-----BORROW A BOOK-----'''
def borrow_book():
    title = input("Enter Book Title: ").lower().strip()
    for book in books:
        if book['Title'] == title and book['Is_Available'] == True:
            book['Is_Available'] = False
            print("Book Borrowed Successfully !")
        elif book['Title'] == title and book['Is_Available'] == False:
            print("Sorry, this book is already borrowed.")
        else:
            print("Book Not Found !")

'''-----RETURN A BOOK-----'''
def return_book():
    title = input("Enter Book Title: ").lower().strip()
    for book in books:
        if book['Title'] == title and book['Is_Available'] == False:
            book['Is_Available'] = True
            print("Thank for returning book !")



'''-----MAIN-----'''
while True:
    print("=====Library Management System=====")
    user_choice = input("1. Add new Book\n2. Search a Book\n3. Display all books\n4. Borrow a Book\n5. Return a Book\n6. Exit\nEnter your choice : ")

    match user_choice:
        case "1":
            add_book()
        case "2":
            search_book()
        case "3":
            display_books()
        case "4":
            borrow_book()
        case "5":
            return_book()
        case "6":
            print("Thanks for Visiting.")
            break