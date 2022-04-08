books = [str(x) for x in input().split("&")]

while True:
	cmd = input()
	explode = cmd.split(" | ")
	try:
		task = explode[0]
		value = explode[1]
	except IndexError:
		pass
	if cmd == "Done":
		break
	if task == "Add Book":
		if value in books:
			pass
		else:
			books.insert(0, value)
	elif task == "Take Book":
		if value not in books:
			pass
		else:
			books.remove(value)
	elif task == "Swap Books":
		book_1 = value
		book_2 = explode[2]
		if book_1 not in books or book_2 not in books:
			pass
		else:
			index_1 = books.index(book_1)
			index_2 = books.index(book_2)
			books[index_1], books[index_2] = books[index_2], books[index_1]
	elif task == "Insert Book":
		if value in books:
			pass
		else:
			books.append(value)
	elif task == "Check Book":
		for ind, val in enumerate(books):
			if ind == int(value):
				print(val)

print(*books, sep=", ")
