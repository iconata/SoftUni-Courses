first_list = input().split(", ")
second_list = input()
result = [el for el in first_list if el in second_list]
print(result)
