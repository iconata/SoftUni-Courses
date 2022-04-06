text = input()

command = input()

while command != "Travel":
	explode = command.split(":")
	task = explode[0]

	if task == "Add Stop":
		index = int(explode[1])
		added_str = explode[2]
		before = text[:index]
		after = text[index:]
		text = before + added_str + after
		print(text)
	elif task == "Remove Stop":
		start = int(explode[1])
		end = int(explode[2]) + 1
		text = text[:start] + text[end:]
		print(text)
	elif task == "Switch":
		old_str = explode[1]
		new_str = explode[2]
		text = text.replace(old_str, new_str)
		print(text)
	command = input()

print(f"Ready for world tour! Planned stops: {text}")
