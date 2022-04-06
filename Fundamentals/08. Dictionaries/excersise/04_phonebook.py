contact = input()
phonebook = dict()

while "-" in contact:
	explode = contact.split("-")
	key = explode[0]
	value = explode[1]
	if key not in phonebook:
		phonebook[key] = value
	phonebook[key] = value
	contact = input()

lines = int(contact)
for _ in range(lines):
	person = input()
	if person in phonebook.keys():
		for name, num in phonebook.items():
			if person == name:
				print(f"{name} -> {num}")
				break
	else:
		print(f'Contact {person} does not exist.')
