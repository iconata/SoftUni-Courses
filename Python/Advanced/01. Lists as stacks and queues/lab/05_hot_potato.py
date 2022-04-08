from collections import deque


people = input().split(" ")
players = deque(people)
potato_jump = int(input())
counter = 0

while len(players) > 1:
    counter += 1
    current_player = players.popleft()
    
    if counter == potato_jump:
        print(f'Removed {current_player}')
        counter = 0
    else:
        players.append(current_player)
print(f'Last is {players.pop()}')
