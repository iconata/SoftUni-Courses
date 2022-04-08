num_of_rooms = int(input())
remaining_chairs = 0
chairs_left = True
for chairs in range(1, num_of_rooms + 1):
	explode =[str(x) for x in input().split(" ")]
	if len(explode[0]) < int(explode[1]):
		needed_chairs_in_room = int(explode[1]) - len(explode[0])
		print(f"{needed_chairs_in_room} more chairs needed in room {chairs}")
		chairs_left = False
	else:
		remaining_chairs += abs(int(explode[1]) - len(explode[0]))
		# chairs_left = True

if chairs_left:
	print(f"Game On, {remaining_chairs} free chairs left")
