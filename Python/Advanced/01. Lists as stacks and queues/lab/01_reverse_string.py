text = input()
before = []
after = []
for let in text:
	before.append(let)

while before:
	after.append(before.pop())

print(*after, sep="")
