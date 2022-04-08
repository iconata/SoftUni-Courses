budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
milk_price = (flour_price * 1.25) / 4
bread_price = flour_price + eggs_price + milk_price
colored_eggs = 0
loaves = 0

while bread_price < budget:
	loaves += 1
	colored_eggs += 3
	budget -= bread_price
	if loaves % 3 == 0:
		colored_eggs -= (loaves - 2)
money_left = budget
print(f'You made {loaves} loaves of Easter bread! Now you have {colored_eggs} '
	f'eggs and {money_left:.2f}BGN left.')