#calculator code

#addition
def add(x,y):
    return x + y

#subtraction
def subtract(x,y):
    return x - y

#multiplication
def multiply(x,y):
    return x * y

#division
def divide(x,y):
    return x / y

#square numbers
def sqr(x):
    return x * x

#cube numbers
def cube(x):
    return x * x * x

#reciprocal
def reci(x):
    return 1 / x

#multiply by pi
def pi(x):
    return x * 3.14

#Square-root
def sqrt(x):

    import math

    return math.sqrt(x)

#input (selecting operation)
print("Select operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square")
print("6. Cube")
print("7. Reciprocal")
print("8. Multiply by pi")
print("9. Square-root")

#output after operation is selected
while True:
    choice = input("Enter choice (1/2/3/4/5/6/7/8/9)")

    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):

        if choice == '1':
            addamount1 = float(input("Enter the first number you need to add: "))
            addamount2 = float(input("Enter the second number you need to add: "))
            print(addamount1, "+", addamount2, "=", add(addamount1, addamount2))

        elif choice == '2':
            subamount1 = float(input("Enter the first number you need to subtract: "))
            subamount2 = float(input("Enter the second number you need to subtract: "))
            print(subamount1, "-", subamount2, "=", subtract(subamount1, subamount2))

        elif choice == '3':
            multiamount1 = float(input("Enter the first number you need to multiply: "))
            multiamount2 = float(input("Enter the second number you need to multiply: "))
            print(multiamount1, "x", multiamount2, "=", multiply(multiamount1, multiamount2))

        elif choice == '4':
            divamount1 = float(input("Enter the first number you need to divide: "))
            divamount2 = float(input("Enter the second number you need to divide: "))
            print(divamount1, "/", divamount2, "=", divide(divamount1, divamount2))

        elif choice == '5':
            sqramount1 = float(input("Enter your number that needs to be squared: "))
            print(sqramount1, "^2", "=", sqr(sqramount1))

        elif choice == '6':
            cubeamount1 = float(input("Enter your number that needs to be cubed: "))
            print(cubeamount1, "^3", "=", cube(cubeamount1))

        elif choice == '7':
            reciamount1 = float(input("Enter your number that needs to be divided by 1: "))
            print("1", "/", reciamount1, "=", reci(reciamount1))

        elif choice == '8':
            piamount1 = float(input("Enter your number that needs to be multiplied by pi: "))
            print(piamount1, "x", "pi", "= about", pi(piamount1))

        elif choice == '9':
            sqrtamount1 = float(input("Enter your number that needs to be square-rooted: "))
            print(sqrtamount1, "sqrt", "=", sqrt(sqrtamount1))
    else:
        print("Invalid Input")
