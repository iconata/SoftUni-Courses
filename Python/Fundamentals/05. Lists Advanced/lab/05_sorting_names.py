names = [item for item in input().split(", ")]
sorted_list = sorted(names, key=lambda x: (-len(x), x))

print(sorted_list)
