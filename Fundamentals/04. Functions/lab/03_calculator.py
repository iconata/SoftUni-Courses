def calculator(operator, a, b):
    if operator == "divide":
        return a / b
    elif operator == "multiply":
        return a * b
    elif operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b


print(int(calculator(operator=input(), a=int(input()), b=int(input()))))
