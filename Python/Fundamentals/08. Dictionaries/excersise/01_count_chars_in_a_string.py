string = input()
new_string = string.replace(" ", "")
chars = dict()
for i in new_string:
	if i not in chars:
		chars[i] = 0
	chars[i] += 1

for key, value in chars.items():
	print(f"{key} -> {value}")
