numberA = float(input("Write number A: "))
numberB = float(input("Write number B: "))
result = None
match input("Available operations: +, -, *, /, power, root. Choose operation: "):
    case '+':
        result =numberA+numberB
    case '-':
        result =numberA-numberB
    case '*':
        result =numberA*numberB
    case '/':
        if numberB == 0:
            print("infinity")
        else:
            result =numberA/numberB
    case 'power':
        result =numberA**numberB
    case 'root':
        result = pow(numberA, 1/numberB)
if result != None:
    print(round(result, 2))
