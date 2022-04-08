number_list = list(map(int, input().split(" ")))
sorted_list = sorted(number_list)
min_number, max_number, sum_of_numbers = sorted_list[0], sorted_list[-1], sum(sorted_list)

print(f"The minimum number is {min_number}")
print(f"The maximum number is {max_number}")
print(f"The sum number is: {sum_of_numbers}")


nums_list = [int(x) for x in input().split(" ")]
min_number, max_number, sum_of_numbers = min(nums_list), max(nums_list), sum(nums_list)

print(f"The minimum number is {min_number}")
print(f"The maximum number is {max_number}")
print(f"The sum number is: {sum_of_numbers}")
