def extract_file(data):
	explode = data.split("\\")
	file = explode[-1].split(".")
	name = file[0]
	extension = file[1]
	print(f'File name: {name}')
	print(f'File extension: {extension}')


filename = input()
extract_file(filename)
