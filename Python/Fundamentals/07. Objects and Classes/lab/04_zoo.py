class Zoo:
	__animals = 0

	def __init__(self, zooname):
		self.zooname = zooname
		self.mammals = []
		self.fishes = list()
		self.birds = list()

	def add_animal(self, species, name):

		if species == "mammal":
			self.mammals.append(name)
			self.__animals += 1
		elif species == "fish":
			self.fishes.append(name)
			self.__animals += 1
		elif species == "bird":
			self.birds.append(name)
			self.__animals += 1

	def get_info(self, species):
		if species == "mammal":
			print(f"{species.capitalize()}s in {self.zooname}: {', '.join(self.mammals)}")
			print(f"Total animals: {self.__animals}")
		elif species == "fish":
			print(f"{species.capitalize()}es in {self.zooname}: {', '.join(self.fishes)}")
			print(f"Total animals: {self.__animals}")
		elif species == "bird":
			print(f"{species.capitalize()}s in {self.zooname}: {', '.join(self.birds)}")
			print(f"Total animals: {self.__animals}")


name = input()
lines = int(input())
zoo = Zoo(name)
for x in range(lines):
	animals = input().split(" ")
	zoo.add_animal(animals[0], animals[1])
species = input()
if species in ("mammal", "fish", "bird"):
	zoo.get_info(species)
