number_of_lines = int(input())
best_snowball = ''
snowball = 0
for ball in range(number_of_lines):
	snowball_weight = int(input())
	snowball_time = int(input())
	snowball_quality = int(input())
	current_snowball = int((snowball_weight / snowball_time) ** snowball_quality)
	if snowball < current_snowball:
		snowball = current_snowball
		best_snowball = f'{snowball_weight} : {snowball_time} = {current_snowball} ({snowball_quality})'
print(best_snowball)