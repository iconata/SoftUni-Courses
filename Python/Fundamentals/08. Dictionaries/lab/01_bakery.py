inventory = input().split(" ")
bakery = dict()

for i in range(0, len(inventory), 2):
	key = inventory[i]
	value = inventory[i + 1]
	bakery[key] = int(value)

print(bakery)
