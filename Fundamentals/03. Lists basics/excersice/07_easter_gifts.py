presents_list = [str(x) for x in input().split(" ")]
command = input().split(" ")
edited_list = presents_list.copy()
final_string = ""

while command != ["No", "Money"]:
    if command == ["No", "Money"]:
        break
    if command[0] == "OutOfStock" and command[1] in presents_list:
        for index, item in enumerate(edited_list):
            if item == command[1]:
                edited_list[index] = "None"
    if command[0] == "Required":
        for ind, it in enumerate(edited_list):
            if ind == int(command[2]):
                edited_list[ind] = command[1]
    if command[0] == "JustInCase":
        edited_list[-1] = command[1]
    command = input().split(" ")

for item in edited_list:
    if item != "None":
        final_string += f"{item} "
final_string = final_string[:-1]
print(final_string)
