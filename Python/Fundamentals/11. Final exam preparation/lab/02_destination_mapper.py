import re
text = input()

regex = r"([=/])([A-Z][A-Za-z]{2,})\1"
matches = re.finditer(regex, text)
destinations = list()
points = 0

for things in matches:
	city = things[2]
	destinations.append(city)
	points += len(city)

output_locations = ', '.join(destinations)
print(f"Destinations: {output_locations}")
print(f"Travel Points: {points}")
