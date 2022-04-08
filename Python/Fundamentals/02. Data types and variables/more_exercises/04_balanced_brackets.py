num = int(input())
balanced = True
opening_bracket = 0
closing_bracket = 0

for i in range(num):
	symbol = input()
	if symbol == '(' or symbol == '((' or symbol == '(((' or symbol == '((((':
		opening_bracket += 1 * len(symbol)
	if symbol == ')' or symbol == '))' or symbol == ')))' or symbol == '))))':
		closing_bracket += 1 * len(symbol)

if opening_bracket == closing_bracket:
	balanced = True
	print("BALANCED")
else:
	balanced = False
	print("UNBALANCED")
