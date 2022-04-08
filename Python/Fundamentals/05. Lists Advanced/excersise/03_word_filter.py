words = [str(x) for x in input().split(" ") if len(x) % 2 == 0]
print(*words, sep="\n")
