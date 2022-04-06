employees_dict = {}

command = input()

while "->" in command:
	explode = command.split(" -> ")
	username = explode[0]
	id_num = explode[1]

	if username not in employees_dict:
		employees_dict[username] = [id_num]
	if id_num not in employees_dict[username]:
		employees_dict[username].append(id_num)
	command = input()

for key, value in employees_dict.items():
	print(f"{key}")
	for items in value:
		print(f"-- {items}")
