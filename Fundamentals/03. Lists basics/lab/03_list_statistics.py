n = int(input())

sum_of_negatives = 0
positives = []
negatives = []
for _ in range(n):
	number = int(input())
	if number >= 0:
		positives.append(number)
	elif number < 0:
		negatives.append(number)
		sum_of_negatives += number

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum_of_negatives}")