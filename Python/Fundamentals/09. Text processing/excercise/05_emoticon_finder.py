def emoticon_finder(data):
	emoticon_list = [text[i] + text[i+1] for i in range(len(data)) if text[i] == ':' and text[i+1] != ' ']
	print(*emoticon_list, sep="\n")


text = input()
emoticon_finder(text)
