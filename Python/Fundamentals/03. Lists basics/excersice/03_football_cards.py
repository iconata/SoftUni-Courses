info = input().split(" ")
team_a_players = 11
team_b_players = 11
lost_players = []
less_players = False

for card in info:
	if card not in lost_players:
		lost_players.append(card)
		if "A" in card:
			team_a_players -= 1
			if team_a_players < 7:
				less_players = True
		if "B" in card:
			team_b_players -= 1
			if team_b_players < 7:
				less_players = True
	if less_players:
		break
print(f"Team A - {team_a_players}; Team B - {team_b_players}")
if less_players:
	print(f"Game was terminated")