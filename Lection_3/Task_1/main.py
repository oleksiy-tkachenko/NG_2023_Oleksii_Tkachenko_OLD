def division(numberA, numberB):
    if numberB == 0:
        print("infinity")
    else:
        return numberA/numberB

def choiceCalculs(numberA, numberB):
    calcResult = None
    match input("Available operations: +, -, *, /, power, root. Choose operation: "):
        case '+':
            calcResult =numberA+numberB
        case '-':
            calcResult =numberA-numberB
        case '*':
            calcResult =numberA*numberB
        case '/':
            calcResult = division(numberA, numberB)
        case 'power':
            calcResult =numberA**numberB
        case 'root':
            calcResult = pow(numberA, 1/numberB)
    return calcResult

finalResult =  choiceCalculs(float(input("Write number A: ")), float(input("Write number B: ")))
if finalResult != None:
    print(round(finalResult, 2))