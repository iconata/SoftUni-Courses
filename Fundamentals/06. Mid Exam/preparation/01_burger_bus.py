num_of_cities = int(input())
city_counter = 0
city_income = 0
total_income = 0
income_list = []

for city in range(num_of_cities):
	town = input()
	city_counter += 1
	city_income = 0
	for _ in range(1, 3):
		income = float(input())
		income_list.append(income)
		if len(income_list) == 2:
			if city_counter % 5 == 0:
				income_list[0] -= income_list[0] * 0.10
			elif city_counter % 3 == 0:
				income_list[1] += income_list[1] * 0.50
			city_income += income_list[0] - income_list[1]
			income_list = []
	total_income += city_income
	print(f"In {town} Burger Bus earned {city_income:.2f} leva.")

print(f"Burger Bus total profit: {total_income:.2f} leva.")
