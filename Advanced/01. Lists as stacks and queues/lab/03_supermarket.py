import sys
from collections import deque
from io import StringIO

people = deque()

input1 = """George
Peter
William
Paid
Michael
Oscar
Olivia
Linda
End"""

input2 = """Anna
Emma
Alexander
End
"""

# sys.stdin = StringIO(input2)

while True:
	command = input()
	if command == "End":
		print(f'{len(people)} people remaining.')
		break
	if command == "Paid":
		while people:
			print(people.pop())
	else:
		people.appendleft(command)
