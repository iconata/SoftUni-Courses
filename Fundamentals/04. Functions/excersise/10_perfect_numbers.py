def perfect_number_check(number):
    sum_of_digits = 0
    for x in range(1, number):
        if number % x == 0:
            sum_of_digits += x
    if sum_of_digits == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


nums = int(input())
perfect_number_check(nums)
