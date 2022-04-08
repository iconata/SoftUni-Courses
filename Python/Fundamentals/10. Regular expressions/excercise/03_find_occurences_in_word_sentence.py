import re
line = input()
searched_word = input()
pattern = rf'\b{searched_word}\b'
matches = re.findall(pattern, line, re.IGNORECASE)
print(len(matches))
