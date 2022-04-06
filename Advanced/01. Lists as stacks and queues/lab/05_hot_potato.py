people = [str(x) for x in input().split(" ")]
turns = int(input())

while people:
    for kid in range(turns):
        people.pop(kid)
        people.insert(0, kid)
    print(f'Removed {kid}')
