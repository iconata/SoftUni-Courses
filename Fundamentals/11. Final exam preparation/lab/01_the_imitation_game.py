# text = [str(x) for x in input()]
#
# command = input()
# while command != "Decode":
# 	explode = command.split("|")
# 	task = explode[0]
# 	value = explode[1]
# 	if task == "Move":
# 		for item in text[:int(value)]:
# 			text.append(item)
# 			text.remove(item)
# 	elif task == "Insert":
# 		index = int(value)
# 		word = explode[2]
# 		text.insert(index, word)
# 	elif task == "ChangeAll":
# 		letter = explode[2]
# 		for i, v in enumerate(text):
# 			if v == value:
# 				text[i] = letter
# 	command = input()
# print(f'The decrypted message is: {"".join(text)}')


text = input()

command = input()
while command != "Decode":
	explode = command.split("|")
	task = explode[0]
	if task == "Move":
		value = int(explode[1])
		static_part = text[value:]
		moving_part = text[:value]
		text = static_part + moving_part
	elif task == "Insert":
		index = int(explode[1])
		value = explode[2]
		before = text[:index]
		after = text[index:]
		text = before + value + after
	elif task == "ChangeAll":
		substr = explode[1]
		letter = explode[2]
		text = text.replace(substr, letter)
	command = input()
print(f'The decrypted message is: {text}')
