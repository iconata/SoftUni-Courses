products = input().split(" ")
searched_items = input().split(" ")
my_dict = dict()

for i in range(0, len(products), 2):
	key = products[i]
	value = products[i + 1]
	my_dict[key] = int(value)

for item in searched_items:
	if item in my_dict:
		print(f"We have {my_dict[item]} of {item} left")
	else:
		print(f"Sorry, we don't have {item}")
