positions = [int(x) for x in input().split(" ")]

while True:
	command = input()
	if command == "End":
		break
	task = command.split(" ")
	index, value = int(task[1]), int(task[2])
	if task[0] == "Shoot":
		try:
			positions[index] = positions[index] - value
			if positions[index] <= 0:
				positions.pop(index)
		except IndexError:
			pass
	elif task[0] == "Add":
		try:
			if index > (len(positions) - 1):
				raise IndexError
			else:
				positions.insert(index, value)
		except IndexError:
			print("Invalid placement!")
	elif task[0] == "Strike":
		try:
			radius = value
			before_radius = index - radius
			after_radius = index + radius
			if before_radius < 0 or after_radius > len(positions):
				raise IndexError
			else:
				del positions[before_radius:after_radius + 1]
		except IndexError:
			print("Strike missed!")

print(*positions, sep="|")
