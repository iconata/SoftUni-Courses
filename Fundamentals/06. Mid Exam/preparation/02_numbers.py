nums = [x for x in input().split(" ")]


while True:
	cmd = input()
	if cmd == "Finish":
		break
	explode = cmd.split(" ")
	task = explode[0]
	value = explode[1]
	if task == "Add":
		nums.append(value)
	elif task == "Remove":
		if value in nums:
			nums.remove(value)
		else:
			pass
	elif task == "Replace":
		if value in nums:
			value_2 = explode[2]
			ind_1 = nums.index(value)
			nums[ind_1] = value_2
		else:
			pass
	elif task == "Collapse":
		nums[:] = filter(lambda x: int(x) > int(value), nums)

print(*nums, sep=" ")
