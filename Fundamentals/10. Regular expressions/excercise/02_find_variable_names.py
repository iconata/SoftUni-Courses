import re

pattern = r'\b_([a-zA-Z]+)\b'
output = []
text = input()
matches = re.finditer(pattern, text)
for items in matches:
	match = items.group(1)
	output.append(match)

print(','.join(output))
