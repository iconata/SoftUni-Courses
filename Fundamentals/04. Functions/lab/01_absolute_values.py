numbers = input().split(" ")
abs_list = list()

for i in numbers:
    absolute = abs(float(i))
    abs_list.append(absolute)

print(abs_list)
