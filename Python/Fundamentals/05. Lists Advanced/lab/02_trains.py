num_of_wagons = int(input())
train_list = [0] * num_of_wagons
copy_train_list = train_list.copy()
command = input().split(" ")

while command != ["End"]:
    if command == ["End"]:
        break
    if command[0] == "add":
        people_getting_on = int(copy_train_list[-1]) + int(command[1])
        copy_train_list.pop(-1)
        copy_train_list.append(people_getting_on)
    if command[0] == "insert":
        people_on_wagon = int(copy_train_list[int(command[1])]) + int(command[2])
        copy_train_list.pop(int(command[1]))
        copy_train_list.insert(int(command[1]), people_on_wagon)
    if command[0] == "leave":
        for index, item in enumerate(copy_train_list):
            if int(command[1]) == index:
                remainder = int(copy_train_list[index]) - int(command[2])
                copy_train_list.pop(index)
                copy_train_list.insert(index, remainder)
    command = input().split(" ")

print(copy_train_list)
