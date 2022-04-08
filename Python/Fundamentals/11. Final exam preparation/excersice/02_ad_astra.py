import re

text = input()
matches = re.findall(r"\#([a-z A-Z]+)\#(\d{2}\/\d{2}\/\d{2})\#(\d+)\#|\|([a-z A-Z]+)\|(\d{2}\/\d{2}\/\d{2})\|(\d+)\|", text)
new_list = []
calories = 0
for items in matches:
	current_item = [i for i in items if i != '']
	new_list.append(current_item)
	calories += int(current_item[2])
available_food = int(calories / 2000)
print(f"You have food to last you for: {available_food} days!")
for thing in new_list:
	product = thing[0]
	exp_date = thing[1]
	cals = thing[2]
	print(f"Item: {product}, Best before: {exp_date}, Nutrition: {cals}")
