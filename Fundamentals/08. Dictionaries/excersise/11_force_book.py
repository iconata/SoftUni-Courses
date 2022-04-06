force_dict = {}

command = input()

while command != "Lumpawaroo":
	explode = command.split(" ")
	delimeter = explode[1]
	if delimeter == "|":
		force_side = explode[0]
		force_user = explode[2]
		if force_user not in force_dict and force_side not in force_dict:
			force_dict[force_side] = [force_user]
		elif force_user not in force_dict.values():
			for value in force_dict.values():
				if value not in force_dict.values():
					force_dict[force_side].append(force_user)
	elif delimeter == "->":
		force_user = explode[0]
		force_side = explode[2]
		for key in force_dict.keys():
			if force_user in force_dict.values():
				force_dict.pop(key)
		if force_user not in force_dict and force_side not in force_dict:
			force_dict[force_side] = [force_user]
		elif force_user not in force_dict.values():
			for value in force_dict.values():
				if value not in force_dict.values():
					force_dict[force_side].append(force_user)

	command = input()


print(force_dict)
