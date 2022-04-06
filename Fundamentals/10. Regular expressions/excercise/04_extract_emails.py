import re

user = r'\b([A-z0-9]+[A-z0-9]+|[A-z0-9]+[_.-]{1}[A-z0-9]+(?<![-._]) )@([A-z][-]?[A-z]+\.[A-z]+)\.?([A-z]+?)\b'
host = r''
output = []
text = input()
matches = re.finditer(user, text)
for items in matches:
	match = items.group()
	output.append(match)

print('\n'.join(output))
