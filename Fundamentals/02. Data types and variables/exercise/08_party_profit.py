group_size = int(input())
days = int(input())
total_coins = 0
companions = group_size

for num in range(1, days + 1):
	total_coins += 50
	if num % 10 == 0:
		companions -= 2
	if num % 15 == 0:
		companions += 5
	total_coins -= companions * 2
	if num % 3 == 0:
		total_coins -= companions * 3
	if num % 5 == 0:
		total_coins += companions * 20
		if num % 3 == 0:
			total_coins -= companions * 2
print(f'{companions} companions received {int(total_coins / companions)} coins each.')