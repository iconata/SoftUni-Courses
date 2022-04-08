numbers_list = [int(x) for x in input().split(", ")]
beggars = int(input())
beggars_list = [0] * beggars


for x in range(len(beggars_list)):
	current_beggar = x
	for y in range(len(numbers_list)):
		current_num = y % beggars
		if current_num == current_beggar:
			if beggars_list[x] == 0:
				if numbers_list[y] == 0:
					beggars_list[current_num] = 0
					break
				beggars_list[current_num] = numbers_list[y]
			else:
				beggars_list[current_num] += numbers_list[y]

print(beggars_list)
