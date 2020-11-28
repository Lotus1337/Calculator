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

#output after num1 and num2 are entered
while True:
    choice = input("Enter choice(1/2/3/4/5/6/7/8)")

    if choice in ('1', '2', '3', '4', '5', '6', '7', '8'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number (If choice is 5, 6, 7, or 8 just enter 1): "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "x", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "^2", "=", sqr(num1))

        elif choice == '6':
            print(num1, "^3", "=", cube(num1))

        elif choice == '7':
            print("1", "/", num1, "=", reci(num1))

        elif choice == '8':
            print(num1, "x", "pi", "= about", pi(num1))
    else:
        print("Invalid Input")
