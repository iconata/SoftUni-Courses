nums = [int(x) for x in input().split(" ")]
middle = int(len(nums) / 2)

sum_of_left_cars = 0
sum_of_right_cars = 0

for left_cars in nums[:middle]:
    if left_cars != 0:
        sum_of_left_cars += left_cars
    elif left_cars == 0:
        sum_of_left_cars *= 0.8

for right_cars in nums[middle + 1:]:
    if right_cars != 0:
        sum_of_right_cars += right_cars
    elif right_cars == 0:
        sum_of_right_cars *= 0.8

if sum_of_left_cars > sum_of_right_cars:
    print(f"The winner is right with total time: {sum_of_right_cars:.1f}")
else:
    print(f"The winner is left with total time: {sum_of_left_cars:.1f}")
