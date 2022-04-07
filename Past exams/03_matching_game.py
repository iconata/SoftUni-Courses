num_string = input().split()

command = input()
moves_counter = 0

while command != "end":
    explode = command.split()
    match1 = int(explode[0])
    match2 = int(explode[1])
    val1 = num_string[match1]
    val2 = num_string[match2]
    moves_counter += 1

    if val1 == val2:
        print(f"Congrats! You have found matching elements - ${val1}!")
        if len(num_string) == 2:
            num_string.clear()
            print(f'You have won in {moves_counter} turns!')
            break
        
        else:
            for value in num_string:
                if value == val2:
                    num_string.remove(value)

    elif match1 < 0 or match2 < 0:
        print(f'Invalid input! Adding additional elements to the board')
        middle = int(len(num_string) / 2)
        char_to_add = f'-{moves_counter}a'
        for items in range(2):
            num_string.insert(middle, char_to_add)
    
    command = input()

print(num_string)
