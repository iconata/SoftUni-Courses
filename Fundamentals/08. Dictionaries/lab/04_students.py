students = dict()
command = input()

while ":" in command:
	explode = command.split(":")
	k = explode[1]
	v = [explode[0], explode[2]]
	students[k] = v
	command = input()

command = command.replace("_", " ")
for key, value in students.items():
	if value[1] == command:
		print(f"{value[0]} - {key}")
