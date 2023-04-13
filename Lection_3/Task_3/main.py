def bookElementSubstitute(elementName):
    books[chosenBookName][elementName] = input(f"To which one?\n{elementName}: ")
    print("======================")

def bookEdit():
    match input("Editing...\n1. Book name\n2. Book author\n3. Page count\n4. Book genre\n5. Book cover\n\n"):
        case '1':
            # making new book with new name and adding previous params to it
            books[input("To which one?\nBook name: ")] = books[chosenBookName]
            # deleting previous book 
            del books[chosenBookName]
            print("======================")
        case '2':
            bookElementSubstitute('Book author')
        case '3':
            bookElementSubstitute('Page count')                    
        case '4':
            bookElementSubstitute('Book genre')
        case '5':
            bookElementSubstitute('Book cover')

def bookNotFound():
    print("No such book found...")
    print("======================")  

def addBook():
    inputBookName = input("Enter name of the book: ")
    if inputBookName in books:
        print("Book with that name already exists.")
        print("======================")
    else:
        books[inputBookName] = {
            'Book author':input("Enter author of the book: "),
            'Page count':input("Enter page count of the book: "),
            'Book genre':input("Enter genre of the book: "),
            'Book cover':input("Enter binding of the book (Soft or Hard): ")
        }
        print("======================")

def printBookDescription(bookName):
    print(f"""Book author: {books[bookName]['Book author']}
Page count: {books[bookName]['Page count']}
Book genre: {books[bookName]['Book genre']}
Book cover: {books[bookName]['Book cover']}""")
    print("======================")

def searchBook():
    match input("List...\n1. All books\n2. The book by name\n"):
        case '1': # prints every book with number
            bookNumber = 1
            for bookName in books:
                print(f"#{bookNumber} Book name: {bookName}")
                printBookDescription(bookName)
        case '2': # searching and printing book by name
            bookName = input("Which one?\nBook name: ")
            if bookName in books:
                printBookDescription(bookName)
            else:
                bookNotFound()

def showMenu():
    print("Menu:\n1. Add a book\n2. Remove a book\n3. Edit book\n4. Scan for books\n5. Show menu\n6. Exit\n")

books = {} # dictionary of books, with name of books as keys
active = True # switch
showMenu()
while active: # while switch is on
    match input("Enter the number of chosen option: "):
        case '1': # adding a book, relying on user input
            addBook()
        case '2': # removing a book, with an exception for unexisting books
            removingBookName = input("Which one?\nBook name: ")
            if removingBookName in books:
                del books[removingBookName]
                print("Done!")
                print("======================")
            else:
                bookNotFound()
        case '3': # editing a book with multiple choices, with an exception for unexisting books
            chosenBookName = input("Which book?\nBook name: ")
            if chosenBookName in books:
                bookEdit()
            else:
                bookNotFound()
        case '4': # scanning for books with choices for all books or one particular
            if len(books) != 0: # if there are any books
                searchBook()
            else:
                print("There are no books at the moment")
                print("======================")
        case '5':
            showMenu()
        case '6': # switching off to exit
            active = False