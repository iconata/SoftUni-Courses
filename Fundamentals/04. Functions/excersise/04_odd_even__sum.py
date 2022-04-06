def odd_even_sum(number):
    odd_sum = 0
    even_sum = 0
    for x in number:
        if int(x) % 2 == 0:
            even_sum += int(x)
        else:
            odd_sum += int(x)
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


odd_even_sum(number=input())


num = input()
even_nums_sum = 0
odd_nums_sum = 0
num_list = list(map(int, num))
for x in num_list:
    if x % 2 == 0:
        even_nums_sum += x
    else:
        odd_nums_sum += x
print(f"Odd sum = {odd_nums_sum}, Even sum = {even_nums_sum}")
