from test import set_year

year = int(input())
is_happy_year = False

while not is_happy_year:
	year += 1
	str_year = str(year)
	set_year = set(str_year)
	if len(set_year) == len(str_year):
		print(year)