words = input().split(" ")
my_dict = dict()

for word in words:
	new_word = word.lower()
	if new_word not in my_dict:
		my_dict[new_word] = 0
	my_dict[new_word] += 1

for key, value in my_dict.items():
	if value % 2 != 0:
		print(key, end=" ")
