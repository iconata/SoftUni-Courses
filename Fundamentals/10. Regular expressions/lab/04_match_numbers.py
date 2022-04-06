import re

text = input()
pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'
matches = re.finditer(pattern, text)

output = []
for items in matches:
	match = items.group()
	output.append(match)

print(' '.join(output))
