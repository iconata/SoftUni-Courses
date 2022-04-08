usernames = input().split(', ')

for name in usernames:
	if name.isalnum():
		if 3 <= len(name) <= 16:
			print(name)
	if "-" in name or '_' in name:
		print(name)
