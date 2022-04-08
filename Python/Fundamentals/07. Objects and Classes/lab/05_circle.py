class Circle:
	__pi = 3.14

	def __init__(self, diameter):
		self.diameter = diameter

	def calculate_circumference(self):
		result = self.__pi * self.diameter
		return result

	def calculate_area(self):
		result = (self.__pi * (self.diameter ** 2)) / 4
		return result

	def calculate_area_of_sector(self, angle):
		result = (angle / 360) * self.__pi * ((self.diameter / 2) ** 2)
		return result


circle = Circle(int(input()))
angle = int(input())

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
