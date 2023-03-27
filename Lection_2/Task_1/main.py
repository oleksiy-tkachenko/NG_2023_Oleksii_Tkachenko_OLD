userInput = input("Please enter elements with which you want to work,"
                  "\nsplitting them by comma and space, like this ', '.\n\n").split(', ')
print('===========================================')
match input("What you want to count?(type the number of the option)\n1. Particular element\n2. All of them\n\n"):
    case '1':
        userElementChoice = input('Which one?\n\n')
        print('===========================================')
        print(f"There are {userInput.count(userElementChoice)} occurrences of {userElementChoice}")
    case '2':
        print('===========================================')
        print(f"There are {len(userInput)} elements total")