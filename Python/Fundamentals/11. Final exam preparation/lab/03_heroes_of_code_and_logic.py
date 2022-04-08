num_of_heroes = int(input())

max_hp = 100
max_mana = 200
heroes_dict = dict()

for _ in range(num_of_heroes):
	hero = input().split()
	name = hero[0]
	hit_points = int(hero[1])
	mana_points = int(hero[2])
	heroes_dict[name] = {'HP': hit_points, 'MP': mana_points}

command = input()
while command != "End":
	explode = command.split(" - ")
	task = explode[0]
	hero_name = explode[1]
	if task == 'Heal':
		heal_amount = int(explode[2])
		current_hp = int(heroes_dict[hero_name]['HP'])
		if (current_hp + heal_amount) > max_hp:
			heal_amount = max_hp - current_hp
			heroes_dict[hero_name]['HP'] = max_hp
		else:
			heroes_dict[hero_name]['HP'] += heal_amount
		print(f'{hero_name} healed for {heal_amount} HP!')
	elif task == 'Recharge':
		mana_recharge_amount = int(explode[2])
		current_mana = int(heroes_dict[hero_name]['MP'])
		if (current_mana + mana_recharge_amount) > max_mana:
			mana_recharge_amount = max_mana - current_mana
			heroes_dict[hero_name]['MP'] = max_mana
		else:
			heroes_dict[hero_name]['MP'] += mana_recharge_amount
		print(f'{hero_name} recharged for {mana_recharge_amount} MP!')
	elif task == 'TakeDamage':
		damage = int(explode[2])
		attacker = explode[3]
		current_hp = heroes_dict[hero_name]['HP']
		hp_remaining = current_hp - damage
		if hp_remaining <= 0:
			heroes_dict.pop(hero_name)
			print(f"{hero_name} has been killed by {attacker}!")
		else:
			heroes_dict[hero_name]['HP'] = hp_remaining
			print(f'{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero_name]["HP"]} HP left!')
	elif task == 'CastSpell':
		mana_cost = int(explode[2])
		spell_name = explode[3]
		current_mana = heroes_dict[hero_name]['MP']
		mana_remaining = current_mana - mana_cost
		if heroes_dict[hero_name]['MP'] >= mana_cost:
			heroes_dict[hero_name]['MP'] = mana_remaining
			print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name]['MP']} MP!")
		else:
			print(f"{hero_name} does not have enough MP to cast {spell_name}!")
	command = input()

for key, value in heroes_dict.items():
	print(key)
	for stat, val in value.items():
		print(f'  {stat}: {val}')
