text = input()
final_str = text

command = input()
while command != "Finish":
	explode = command.split()
	task = explode[0]
	if task == "Replace":
		old_char = explode[1]
		new_char = explode[2]
		final_str = text.replace(old_char, new_char)
		print(final_str)
	elif task == "Cut":
		start_index = int(explode[1])
		end_index = int(explode[2]) + 1
		if start_index < 0 or end_index > len(final_str):
			print(f'Invalid indices!')
		else:
			before = final_str[:start_index]
			after = final_str[end_index:]
			final_str = before + after
			print(final_str)
	elif task == "Make":
		case = explode[1]
		if case == "Lower":
			final_str = final_str.lower()
			print(final_str)
		else:
			final_str = final_str.upper()
			print(final_str)
	elif task == "Check":
		substr = explode[1]
		if substr in final_str:
			print(f'Message contains {substr}')
		else:
			print(f'Message doesn\'t contain {substr}')
	elif task == "Sum":
		start_index = int(explode[1])
		end_index = int(explode[2]) + 1
		if start_index < 0 or end_index > len(final_str):
			print(f'Invalid indices!')
		else:
			substr = final_str[start_index:end_index]
			result = 0
			for i in substr:
				result += ord(i)
			print(result)
	command = input()
