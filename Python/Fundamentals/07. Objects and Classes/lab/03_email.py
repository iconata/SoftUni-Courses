class Email:
	def __init__(self, sender, receiver, content):
		self.sender = sender
		self.receiver = receiver
		self.content = content
		self.is_sent = False

	def sent(self):
		self.is_sent = True

	def get_info(self):
		return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []


while True:
	text = input()
	if text == "Stop":
		break
	else:
		explode = text.split(" ")
		sender = explode[0]
		receiver = explode[1]
		content = explode[2]
		email = Email(sender, receiver, content)
		emails.append(email)

sent_emails = [int(x) for x in input().split(", ")]

for ind in sent_emails:
	emails[ind].sent()

for email in emails:
	print(email.get_info())
