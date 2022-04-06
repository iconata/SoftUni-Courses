def find_wolf(string):
    list_index = 0
    str_explode = list(string.split(", "))
    if str_explode.index("wolf") == len(str_explode) - 1:
        print("Please go away and stop eating my sheep")
    else:
        wolf_locator = list_index
        closest_sheep = wolf_locator + 1
        print(f"Oi! Sheep number {closest_sheep * (len(str_explode) -1)}! You are about to be eaten by a wolf!")


find_wolf(string=input())
