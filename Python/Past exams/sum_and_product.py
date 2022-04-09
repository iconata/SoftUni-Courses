num = int(input())
is_combination = False

for a in range(1, 10):
	if is_combination:
		break

	for b in range(9, a, -1):
		if is_combination:
			break

		for c in range(0, 10):
			if is_combination:
				break

			for d in range(9, c, -1):

				add_result = a+b+c+d
				multiply_result = a*b*c*d

				if add_result == multiply_result and num % 10 == 5:
					print(f"{a}{b}{c}{d}")
					is_combination = True
					break
				
				elif multiply_result // add_result == 3 and num % 3 == 0:
					print(f"{d}{c}{b}{a}")
					is_combination = True
					break
				
if not is_combination:
	print(f'Nothing found')
