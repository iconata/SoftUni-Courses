import re

lines = int(input())
pattern = r'!(\b[A-Z][a-z]{3,}\b)!:\[\b([A-z]{8,})\b\]'
some_dict = {}
for _ in range(lines):
	text = input()
	matches = re.findall(pattern, text)
	if matches != []:
		output = []
		command = matches[0][0]
		message = matches[0][1]
		for x in message:
			output.append(str(ord(x)))
		print(f"{command}: {' '.join(output)}")
	else:
		print(f'The message is invalid')
