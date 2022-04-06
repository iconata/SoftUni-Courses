class Party:
	def __init__(self):
		self.people = list()


party = Party()

while True:
	names = input()
	if names == "End":
		break
	else:
		party.people.append(names)

print(f'Going: {", ".join(party.people)}')
print(f"Total: {len(party.people)}")
