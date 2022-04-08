numbers = list(map(int, input().split(" ")))
even_nums_list = []
for x in numbers:
    if x % 2 == 0:
        even_nums_list.append(x)

print(even_nums_list)


def even_nums(number):
    even_list = list()
    for x in number:
        if x % 2 == 0:
            even_list.append(x)
    print(even_list)


even_nums(map(int, input().split(" ")))
