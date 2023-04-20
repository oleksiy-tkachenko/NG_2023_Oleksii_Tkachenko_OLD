def printFinalResult():
    finalResult =  choiceCalculs(float(input("Write number A: ")), float(input("Write number B: ")))
    if finalResult != None:
        print(round(finalResult, 2))

def division(numberA, numberB):
    if numberB == 0:
        print("infinity")
    else:
        return numberA/numberB

def addition(numberA, numberB):
    return numberA+numberB

def subtraction(numberA, numberB):
    return numberA-numberB

def multiplication(numberA, numberB):
    return numberA*numberB


def choiceCalculs(numberA, numberB):
    calcResult = None
    match input("Available operations: +, -, *, /, power, root. Choose operation: "):
        case '+':
            calcResult = addition(numberA, numberB)
        case '-':
            calcResult = subtraction(numberA, numberB)
        case '*':
            calcResult = multiplication(numberA, numberB)
        case '/':
            calcResult = division(numberA, numberB)
        case 'power':
            calcResult = pow(numberA,numberB)
        case 'root':
            calcResult = pow(numberA, 1/numberB)
    return calcResult

printFinalResult()