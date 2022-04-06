def factorial_division(num1, num2):
    sum_num1 = 1
    sum_num2 = 1
    for x in range(1, num1 + 1):
        sum_num1 *= x
    for y in range(1, num2 + 1):
        sum_num2 *= y
    return sum_num1 / sum_num2


number_1, number_2 = int(input()), int(input())
print(f"{factorial_division(number_1, number_2):.2f}")
