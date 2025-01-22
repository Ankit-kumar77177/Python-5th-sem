while True:
    num1 = input("Enter the first number: ")
    if num1.lower() == "exit":
        break
    num2 = input("Enter the second number: ")
    operator = input("Enter the operator (+, -, *, /): ")
    if operator == "+":
        result = float(num1) + float(num2)
    elif operator == "-":
        result = float(num1) - float(num2)
    elif operator == "*":
        result = float(num1) * float(num2)
    elif operator == "/":
        if float(num2) != 0:
            result = float(num1) / float(num2)
        else:
            print("Error: Division by zero is not allowed.")
            continue
    else:
        print("Error: Invalid operator.")
        continue
    print("The result is: ", result)