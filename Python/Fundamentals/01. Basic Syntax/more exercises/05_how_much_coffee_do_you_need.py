def coffee_needs(task):
    needed_coffee = 0
    while task != "END":
        if task == "END":
            break
        if task in ["cat", "dog", "coding", "movie"]:
            needed_coffee += 1
        elif task in ["CAT", "DOG", "CODING", "MOVIE"]:
            needed_coffee += 2
        task = input()
    if needed_coffee > 5:
        print("You need extra sleep")
    else:
        print(needed_coffee)


coffee_needs(task=input())
