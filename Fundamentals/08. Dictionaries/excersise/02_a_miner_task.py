collection = dict()

while True:
	command = input()
	if command == "stop":
		break
	quantity = int(input())
	if command not in collection:
		collection[command] = 0
	collection[command] += quantity

for key, value in collection.items():
	print(f'{key} -> {value}')
