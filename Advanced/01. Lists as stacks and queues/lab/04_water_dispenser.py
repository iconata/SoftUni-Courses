from collections import deque


total_water = int(input())
people = deque()

command = input()

while command != "Start":
    people.append(command)
    command = input()

command = input()
while command != "End":

    if command.startswith("refill"):
        explode = command.split(" ")
        liters_to_add = int(explode[1])
        total_water += liters_to_add
    else:
        litters_to_remove = int(command)
        if litters_to_remove <= total_water:
            total_water -= litters_to_remove
            print(f"{people.popleft()} got water")
        else:
            print(f'{people.popleft()} must wait')
    command = input()
print(f'{total_water} liters left')
