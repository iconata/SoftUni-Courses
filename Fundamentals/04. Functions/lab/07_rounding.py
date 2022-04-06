def rounder(float_string):
    new_list = list()
    nums_as_string = float_string.split(" ")
    for n in nums_as_string:
        num = round(float(n))
        new_list.append(num)
    return new_list


print(rounder(float_string=input()))