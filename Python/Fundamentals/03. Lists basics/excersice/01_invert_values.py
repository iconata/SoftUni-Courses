text = input().split()
new_list = []
for i in range(len(text)):
	current_index = i
	num_as_int = int(text[i]) * -1
	new_list.append(num_as_int)

print(new_list)