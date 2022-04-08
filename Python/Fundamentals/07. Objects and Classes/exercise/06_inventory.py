class Inventory:
	def __init__(self, __capacity):
		self.__capacity = __capacity
		self.items = list()

	def add_item(self, item):
		if self.__capacity > len(self.items):
			self.items.append(item)
		else:
			return f"not enough room in the inventory"

	def get_capacity(self):
		return self.__capacity

	def __repr__(self):
		capacity_left = abs(len(self.items) - self.__capacity)
		return f"Items: {', '.join(self.items)}.\nCapacity left: {capacity_left}"


inventory = Inventory(6)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
