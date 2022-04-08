countries = input().split(", ")
capitals = input().split(", ")
maps = tuple(zip(countries, capitals))
my_dict = dict(maps)

for country, city in my_dict.items():
	print(f'{country} -> {city}')
