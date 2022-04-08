score = input().split(" ")
factor = int(input())

score = list(map(lambda x: int(x) * factor, score))
filtered_list = list(filter(lambda x: (x >= sum(score) / len(score)), score))
if len(filtered_list) >= len(score) / 2:
    print(f"Score: {len(filtered_list)}/{len(score)}. Employees are happy!")
else:
    print(f"Score: {len(filtered_list)}/{len(score)}. Employees are not happy!")
