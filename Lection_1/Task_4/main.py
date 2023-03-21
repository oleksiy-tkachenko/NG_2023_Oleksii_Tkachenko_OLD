numberA = float(input("Enter the following numbers\n\nv        \nax^2+bx+c: "))
numberB = float(input("\n     v   \nax^2+bx+c: "))
numberC = float(input("\n        v\nax^2+bx+c: "))
discriminant = pow(numberB, 2) - 4 * numberA * numberC 
if discriminant > 0:
    print(f"x1 = {(-numberB+pow(discriminant,1/2))/(2*numberA)},\nx2 = {(-numberB-pow(discriminant,1/2))/(2*numberA)}")
elif discriminant == 0:
    print(f"x = {-numberB/(2*numberA)}")
else:
    print("Discriminant < 0, therefore no roots")