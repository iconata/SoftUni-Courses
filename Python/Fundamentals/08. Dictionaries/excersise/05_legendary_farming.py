from re import M


legendary_mats_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_mats_dict = dict()
legendary_obtained = False

while not legendary_obtained:
	current_line = input().split()
	for i in range(0, len(current_line), 2):
		material_qty = int(current_line[i])
		material = current_line[i+1].lower()
		if material in legendary_mats_dict:
			legendary_mats_dict[material] += material_qty
			if legendary_mats_dict[material] >= 250:
				break
		else:
			if material not in junk_mats_dict.keys():
				junk_mats_dict[material] = material_qty
			else:
				junk_mats_dict[material] += material_qty
	legendary_item = ''
	if legendary_mats_dict['shards'] >= 250:
		legendary_item = 'Shadowmourne'
		legendary_mats_dict['shards'] -= 250
		print(f'{legendary_item} obtained!')
		legendary_obtained = True
	elif legendary_mats_dict['fragments'] >= 250:
		legendary_item = 'Valanyr'
		legendary_mats_dict['fragments'] -= 250
		print(f'{legendary_item} obtained!')
		legendary_obtained = True
	elif legendary_mats_dict['motes'] >= 250:
		legendary_item = 'Dragonwrath'
		legendary_mats_dict['motes'] -= 250
		print(f'{legendary_item} obtained!')
		legendary_obtained = True

for mat, qty in legendary_mats_dict.items():
	print(f'{mat}: {qty}')
for key, val in junk_mats_dict.items():
	print(f'{key}: {val}')
