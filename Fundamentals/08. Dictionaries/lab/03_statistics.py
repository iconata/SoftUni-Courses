products = dict()

while True:
	items = input().split(": ")
	if items[0] == "statistics":
		break
	key = items[0]
	value = items[1]
	if items[0] in products:
		products[key] += int(value)
	else:
		products[key] = int(value)

print(f"Products in stock:")
for product, quantity in products.items():
	print(f"- {product}: {quantity}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
