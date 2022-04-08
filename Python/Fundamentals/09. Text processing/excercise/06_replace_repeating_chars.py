def replace_repeating_chars(data):
	new_string = ''
	previous_char = ''
	for ch in data:
		if previous_char == ch:
			pass
		elif previous_char != ch:
			new_string += ch
		previous_char = ch
	print(new_string)


text = input()
replace_repeating_chars(text)
