people = int(input())
lift_list = [int(x) for x in input().split()]
lift_capacity = (4 * len(lift_list)) - sum(lift_list)
capacity_left = True

for i in range(lift_capacity):
	while lift_list[i] < 4:
		if capacity_left:
			lift_list[i] += 1
			lift_capacity -= 1
			people -= 1
			if lift_capacity == 0 or people == 0:
				capacity_left = False
				break

	if not capacity_left:
		break
if people:
	print(f'There isn\'t enough space! {people} people in a queue!')
	print(*lift_list, sep=" ")
else:
	print(f'The lift has empty spots!')
	print(*lift_list, sep=" ")
