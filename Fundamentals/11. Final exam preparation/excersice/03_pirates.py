text = input()
cities_dict = dict()

while text != "Sail":
	explode = text.split("||")
	city = explode[0]
	population = int(explode[1])
	gold_amount = int(explode[2])
	if city not in cities_dict:
		cities_dict[city] = {'people': population, 'gold': gold_amount}
	else:
		cities_dict[city]['gold'] += gold_amount
		cities_dict[city]['people'] += population
	text = input()

command = input()
while command != "End":
	explode = command.split("=>")
	task = explode[0]
	city = explode[1]
	if task == "Plunder":
		killed = int(explode[2])
		gold_plund = int(explode[3])
		cities_dict[city]['gold'] -= gold_plund
		cities_dict[city]['people'] -= killed
		print(f'{city} plundered! {gold_plund} gold stolen, {killed} citizens killed.')
		if cities_dict[city]['gold'] <= 0 or cities_dict[city]['people'] <= 0:
			del cities_dict[city]
			print(f'{city} has been wiped off the map!')
	elif task == "Prosper":
		gold_inv = int(explode[2])
		if gold_inv < 0:
			print(f'Gold added cannot be a negative number!')
		else:
			cities_dict[city]['gold'] += gold_inv
			print(f'{gold_inv} gold added to the city treasury. {city} now has {cities_dict[city]["gold"]} gold.')
	command = input()

print(f"Ahoy, Captain! There are {len(cities_dict)} wealthy settlements to go to:")
for city in cities_dict.keys():
	print(f'{city} -> Population: {cities_dict[city]["people"]} citizens, Gold: {cities_dict[city]["gold"]} kg')
