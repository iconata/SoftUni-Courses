electrons = int(input())
filled_shells = list()

for el in range(1, electrons + 1):
	result = 2 * (el ** 2)
	other_sum = sum(filled_shells) + result
	if sum(filled_shells) == electrons:
		break
	elif other_sum > electrons:
		remaining_electrons = abs(electrons - sum(filled_shells))
		filled_shells.append(remaining_electrons)
		break
	else:
		filled_shells.append(result)

print(filled_shells)
