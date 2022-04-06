num = int(input())
capacity_left = 255
total_water = 0

for i in range(num):
	water = int(input())
	if water <= capacity_left:
		capacity_left -= water
		total_water += water
		continue
	print('Insufficient capacity!')
print(total_water)