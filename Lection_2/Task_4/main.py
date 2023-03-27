books = {} # dictionary of books, with name of books as keys
active = True # switch

while active: # while switch is on
    match input("Enter the number of chosen option\n1. Add a book\n2. Remove a book\n3. Edit book\n4. Scan for books\n5. Exit\n\n"):
        case '1': # adding a book, relying on user input
            inputBookName = input("Enter name of the book: ")
            books[inputBookName] = {
                    'Book author':input("Enter author of the book: "),
                    'Page count':input("Enter page count of the book: "),
                    'Book genre':input("Enter genre of the book: "),
                    'Book cover':input("Enter binding of the book (Soft or Hard): ")}
            print("======================")
        case '2': # removing a book, with an exception for unexisting books
            removingBookName = input("Which one?\nBook name: ")
            if removingBookName in books:
                del books[removingBookName]
                print("Done!")
                print("======================")
            else:
                print("No such book found...")
                print("======================")
        case '3': # editing a book with multiple choices, with an exception for unexisting books
            chosenBookName = input("Which book?\nBook name: ")
            if chosenBookName in books:
                match input("Editing...\n1. Book name\n2. Book author\n3. Page count\n4. Book genre\n5. Book cover\n\n"):
                    case '1':
                        # making new book with new name and adding previous params to it
                        books[input("To which one?\nBook name: ")] = books[chosenBookName]
                        # deleting previous book 
                        del books[chosenBookName]
                        print("======================")
                    case '2':
                        books[chosenBookName]['Book author'] = input("To which one?\nBook author: ")
                        print("======================")
                    case '3':
                        books[chosenBookName]['Page count'] = input("To which one?\nPage count: ")
                        print("======================")                    
                    case '4':
                        books[chosenBookName]['Book genre'] = input("To which one?\nBook genre: ")
                        print("======================")
                    case '5':
                        books[chosenBookName]['Book cover'] = input("To which one?\nBook cover (Soft or Hard): ")
                        print("======================")
            else:
                print("No such book found...")
                print("======================")
        case '4': # scanning for books with choices for all books or one particular
            if len(books) != 0: # if there are any books
                match input("List...\n1. All books\n2. The book by name\n"):
                    case '1': # prints every book with number
                        bookNumber = 1
                        for bookName in books:
                            print(f"""#{bookNumber} Book name: {bookName}
Book author: {books[bookName]['Book author']}
Page count: {books[bookName]['Page count']}
Book genre: {books[bookName]['Book genre']}
Book cover: {books[bookName]['Book cover']}""")
                            print("======================")
                    case '2': # searching and printing book by name
                        bookName = input("Which one?\nBook name: ")
                        if bookName in books:
                            print(f"""Book author: {books[bookName]['Book author']}
Page count: {books[bookName]['Page count']}
Book genre: {books[bookName]['Book genre']}
Book cover: {books[bookName]['Book cover']}""")
                            print("======================")
                        else:
                            print("No such book found...")
                            print("======================")
            else:
                print("There are no books at the moment")
                print("======================")
        case '5': # switching off to exit
            active = False