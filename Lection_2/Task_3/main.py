print("Write three lines of elements, with each element separated by comma and space(', ')")
userInput = input("1: ").split(', ')+input("2: ").split(', ')+input("3: ").split(', ') # adding all lists in one
for element in set(userInput): # scrolls through every unique element
    if userInput.count(element)>1: # if its non-unique
        print(element, end=', ')