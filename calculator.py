print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")

option = int(input("Choose an operation: "))

if option in [1, 2, 3, 4]:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if option == 1:
        result = num1 + num2
    elif option == 2:
        result = num1 - num2
    elif option == 3:
        result = num1 * num2
    elif option == 4:
        if num2 == 0:
            result = "undefined (division by zero)"
        else:
            result = num1 / num2

    print("The result is: {}".format(result))
else:
    print("Invalid operation entered.")
