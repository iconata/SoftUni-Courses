def smallest_number(a, b, c):
    num_list = [a, b, c]
    num_list.sort()
    return num_list[0]


print(smallest_number(a=int(input()), b=int(input()), c=int(input())))