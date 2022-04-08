nums = [int(x) for x in input().split(", ")]
group_of_tens = []
group_of_twenties = []
group_of_thirties = []
group_of_forties = []
group_of_fifties = []

for num in nums:
	if num <= 10:
		group_of_tens.append(num)
	elif num <= 20:
		group_of_twenties.append(num)
	elif num <= 30:
		group_of_thirties.append(num)
	elif num <= 40:
		group_of_forties.append(num)
	elif num <= 50:
		group_of_fifties.append(num)

print(f"""
Group of 10's: {group_of_tens}
Group of 20's: {group_of_twenties}
Group of 30's: {group_of_thirties}
Group of 40's: {group_of_forties}
Group of 50's: {group_of_fifties}
""")