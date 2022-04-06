import re


pattern = r'\d+'


output = []
while True:
	text = input()
	matches = re.finditer(pattern, text)
	if not text:
		break
	for items in matches:
		match = items.group()
		output.append(match)

print(' '.join(output))
