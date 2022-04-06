text = input()
indices = []

for index, value in enumerate(text):
	if value == "(":
		indices.append(index)
	elif value == ")":
		start = indices.pop()
		end = index + 1
		print(text[start:end])
