def cipher(data):
	crypted_text = ''
	for char in data:
		new_symbol = chr(ord(char) + 3)
		crypted_text += new_symbol
	print(crypted_text)


text = input()
cipher(text)
