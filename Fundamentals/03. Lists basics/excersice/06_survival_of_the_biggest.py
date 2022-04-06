numbers = [int(x) for x in input().split(" ")]
nums_to_remove = int(input())

for x in range(nums_to_remove):
    numbers.remove(min(numbers))

print(numbers)
