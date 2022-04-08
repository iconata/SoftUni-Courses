import string


def change_numbers(data):
	result = []
	for items in data:
		for x in items:
			num = ''
			first_letter = ''
			second_letter = ''
			if x.isdigit():
				num += x
			else:
				if first_letter == '':
					first_letter = x
				else:
					second_letter = x
			if x.isalpha():
				if (x.isupper() or x.islower()) and first_letter == '':
					first_letter = x
					letter_position = string.ascii_letters.index(x)
					if first_letter.isupper():
						calc = int(num)/letter_position
						num = calc
					else:
						calc = int(num)*letter_position
						num = calc
				else:
					second_letter = x
					letter_position = string.ascii_letters.index(x)
					if second_letter.isupper():
						calc = int(num)-letter_position
						num = calc
					else:
						calc = int(num)+letter_position
						num = calc


text = input().split()
change_numbers(text)
