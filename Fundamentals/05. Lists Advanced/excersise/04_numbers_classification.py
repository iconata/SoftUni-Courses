nums = [int(x) for x in input().split(", ")]
positive = []
negative = []
even = []
odd = []

for num in nums:
	if num >= 0:
		positive.append(str(num))
	if num < 0:
		negative.append(str(num))
	if num % 2 == 0:
		even.append(str(num))
	if num % 2 != 0:
		odd.append(str(num))

print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")
