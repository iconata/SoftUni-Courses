products = dict()

command = input()
while " " in command:
	explode = command.split(" ")
	name = explode[0]
	price = float(explode[1])
	quantity = int(explode[2])

	if name not in products:
		products[name] = [price, quantity]
	else:
		products[name] = [price, (quantity + products[name][1])]

	command = input()


for key, value in products.items():
	print(f"{key} -> {value[0]*value[1]:.2f}")
