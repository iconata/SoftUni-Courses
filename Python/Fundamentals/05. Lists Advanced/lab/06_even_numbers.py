nums = [int(x) for x in input().split(", ")]
index_list = []

for index, item in enumerate(nums):
    if item % 2 == 0:
        index_list.append(index)

print(index_list)


numbers = list(map(int, input().split(", ")))
found_evens = map(lambda x: x if numbers[x] % 2 == 0 else "no", range(len(numbers)))
evens = list(filter(lambda a: a != "no", found_evens))
print(evens)
