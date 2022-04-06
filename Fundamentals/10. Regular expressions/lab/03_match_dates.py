import re

text = input()
pattern = r'(\d{2}\/[A-Z][a-z]{2}\/\d{4}\b)|(\d{2}-[A-Z][a-z]{2}-\d{4}\b)|(\d{2}\.[A-Z][a-z]{2}\.\d{4}\b)'
matches = re.finditer(pattern, text)
some_list = []
for i in matches:
	some_list.append(i.group())

for things in some_list:
	if "-" in things:
		explode = things.split("-")
		day = explode[0]
		month = explode[1]
		year = explode[2]
		print(f'Day: {day}, Month: {month}, Year: {year}')
	elif "." in things:
		explode = things.split(".")
		day = explode[0]
		month = explode[1]
		year = explode[2]
		print(f'Day: {day}, Month: {month}, Year: {year}')
	elif "/" in things:
		explode = things.split("/")
		day = explode[0]
		month = explode[1]
		year = explode[2]
		print(f'Day: {day}, Month: {month}, Year: {year}')
