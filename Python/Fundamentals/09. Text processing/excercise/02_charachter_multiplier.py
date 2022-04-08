def sum_func(first, second):
	total_sum = 0
	for i in range(len(first)):
		if i < len(second):
			total_sum += ord(first[i]) * ord(second[i])
		else:
			total_sum += ord(second[i])
	return total_sum


def character_multiplier(data):
	result = 0
	explode = data.split()
	first = explode[0]
	second = explode[1]
	if len(first) > len(second):
		result = sum_func(first, second)
	else:
		result = sum_func(second, first)
	print(result)


text = input()
character_multiplier(text)
