nums = [int(x) for x in input().split(", ")]
final_list = nums.copy()

for x in final_list:
    if x == 0:
        final_list.remove(0)
    if len(nums) != len(final_list):
        final_list.append(0)

print(final_list)
