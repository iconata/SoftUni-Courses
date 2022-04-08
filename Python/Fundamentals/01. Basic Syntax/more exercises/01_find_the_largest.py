def largest_num(num):
    num_list = [str(x) for x in num]
    num_list.sort(reverse=True)
    sorted_num = "".join(num_list)
    return sorted_num


print(largest_num(num=input()))
