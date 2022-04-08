text = [str(x) for x in input().split(" ")]
shuffles = int(input())
shuffled_list = list()
middle = int(len(text) / 2)

for _ in range(shuffles):
    first_half = text[:middle]
    second_half = text[middle:]
    for card in range(len(first_half)):
        shuffled_list.append(first_half[card])
        shuffled_list.append(second_half[card])
    text = shuffled_list
    shuffled_list = list()
print(text)
