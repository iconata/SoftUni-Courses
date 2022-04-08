n = int(input())
word = input()

strings = []
new_strings = []

for _ in range(n):
	sentence = input()
	strings.append(sentence)
	if word in sentence:
		new_strings.append(sentence)

print(strings)
print(new_strings)