capacity = int(input())
users = dict()

command = input()
while command != "Statistics":
	explode = command.split("=")
	task = explode[0]
	if task == "Add":
		username = explode[1]
		msgs_sent = int(explode[2])
		msgs_received = int(explode[3])
		if username not in users:
			users[username] = {'sent': msgs_sent, 'received': msgs_received}
	elif task == "Message":
		sender = explode[1]
		receiver = explode[2]
		if sender in users.keys() and receiver in users.keys():
			users[sender]['sent'] += 1
			users[receiver]['received'] += 1
			if (users[sender]['sent'] + users[sender]['received']) >= capacity:
				print(f'{sender} reached the capacity!')
				del users[sender]
			elif (users[receiver]['received'] + users[receiver]['sent']) >= capacity:
				print(f'{receiver} reached the capacity!')
				del users[receiver]
	elif task == "Empty":
		username = explode[1]
		if username in users.keys():
			del users[username]
		elif username == "All":
			users.clear()
	command = input()

print(f'Users count: {len(users)}')

for key, value in users.items():
	sum_of_msgs = users[key]['sent'] + users[key]['received']
	print(f'{key} - {sum_of_msgs}')
