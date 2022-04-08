parking_dict = dict()
lines = int(input())

for user in range(lines):
	command = input().split(" ")
	task = command[0]
	username = command[1]
	try:
		plate = command[2]
	except IndexError:
		pass

	if task == "register" and username not in parking_dict:
		parking_dict[username] = plate
		print(f"{username} registered {plate} successfully")
	elif task == "register" and username in parking_dict:
		print(f"ERROR: already registered with plate number {plate}")

	elif task == "unregister" and username not in parking_dict:
		print(f"ERROR: user {username} not found")
	else:
		del parking_dict[username]
		print(f"{username} unregistered successfully")

for key, value in parking_dict.items():
	print(f"{key} => {value}")
