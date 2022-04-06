nums_list = [int(x) for x in input().split(" ")]
list_copy = nums_list.copy()

while True:
    command = input()
    if command == "end":
        break
    task = command.split(" ")
    if task[0] == "swap":
        list_copy[int(task[1])], list_copy[int(task[2])] = list_copy[int(task[2])], list_copy[int(task[1])]
    elif task[0] == "multiply":
        list_copy[int(task[1])] = list_copy[int(task[1])] * list_copy[int(task[2])]
    elif task[0] == "decrease":
        for index, value in enumerate(list_copy):
            list_copy[index] = value - 1


print(*list_copy, sep=", ")
