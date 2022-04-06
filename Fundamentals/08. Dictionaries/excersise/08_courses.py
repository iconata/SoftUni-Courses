courses_dict = {}

command = input()

while " " in command:
	explode = command.split(":")
	course_name = explode[0].rstrip()
	student = explode[1]

	if course_name not in courses_dict:
		courses_dict[course_name] = [student]
	else:
		courses_dict[course_name].append(student)
	command = input()

for key, value in courses_dict.items():
	print(f'{key}: {len(value)}')
	for items in value:
		print(f'--{items}')
