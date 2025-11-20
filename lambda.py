add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y

while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter your operation (+, -, *, /): ")

    if operator == "+":
        print(num1, "+", num2, "=", add(num1, num2))
    elif operator == "-":
        print(num1, "-", num2, "=", sub(num1, num2))
    elif operator == "*":
        print(num1, "*", num2, "=", mul(num1, num2))
    elif operator == "/":
        print(num1, "/", num2, "=", div(num1, num2))
    else:
        print("Invalid operator. Please choose from +, -, *, /")
        continue

    next_calc = input("Do you want to do another calculation? (yes/no): ").lower()
    if next_calc != "yes":
        print("Goodbye!")
        break
