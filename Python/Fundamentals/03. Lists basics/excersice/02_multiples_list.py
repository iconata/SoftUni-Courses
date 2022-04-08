factor = int(input())
count = int(input())
num_list = []
for i in range(1, count + 1):
	multiples = i * factor
	num_list.append(multiples)

print(num_list)