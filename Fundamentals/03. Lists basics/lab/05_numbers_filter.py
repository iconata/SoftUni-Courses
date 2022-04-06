iterr = int(input())

positive_nums = []
negative_nums = []
even_nums = []
odd_nums = []

for _ in range(iterr):
	number = int(input())
	if number % 2 == 0:
		even_nums.append(number)
	if number % 2 != 0:
		odd_nums.append(number)
	if number >= 0:
		positive_nums.append(number)
	if number < 0:
		negative_nums.append(number)

command = input()
if command == "even":
	print(even_nums)
elif command == "odd":
	print(odd_nums)
elif command == "positive":
	print(positive_nums)
elif command == "negative":
	print(negative_nums)