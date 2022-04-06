# command = input().split("-")
# final_tasks = [0] * 10
# while command != ["End"]:
#
#     if command == ["End"]:
#         break
#     if int(command[0]) == 1:
#         final_tasks.insert(0, command[1])
#     if int(command[0]) == 2:
#         final_tasks.insert(1, command[1])
#     if int(command[0]) == 3:
#         final_tasks.insert(2, command[1])
#     if int(command[0]) == 4:
#         final_tasks.insert(3, command[1])
#     if int(command[0]) == 5:
#         final_tasks.insert(4, command[1])
#     if int(command[0]) == 6:
#         final_tasks.insert(5, command[1])
#     if int(command[0]) == 7:
#         final_tasks.insert(6, command[1])
#     if int(command[0]) == 8:
#         final_tasks.insert(7, command[1])
#     if int(command[0]) == 9:
#         final_tasks.insert(8, command[1])
#     if int(command[0]) == 10:
#         final_tasks.insert(9, command[1])
#     command = input().split("-")
#
# result = [item for item in final_tasks if item != 0]
# print(result)

final_tasks = [0] * 10
while True:
    command = input()
    if command == "End":
        break
    tasks = command.split("-")
    priority = int(tasks[0]) - 1
    notes = tasks[1]
    final_tasks.pop(priority)
    final_tasks.insert(int(priority), tasks[1])

result = [item for item in final_tasks if item != 0]
print(result)
