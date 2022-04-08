lost_battles = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
gladiator_expenses = 0
broken_shield_count = 0

for battles in range(1, lost_battles + 1):
	if battles % 2 == 0:
		gladiator_expenses += helmet_price
	if battles % 3 == 0:
		gladiator_expenses += sword_price
	if battles % 6 == 0:
		gladiator_expenses += shield_price
		broken_shield_count += 1
		if broken_shield_count == 2:
			gladiator_expenses += armor_price
			broken_shield_count = 0
print(f'Gladiator expenses: {gladiator_expenses:.2f} aureus')