people = [x for x in input().split(" ")]
people_skipped = int(input())

person_executed = []
counter = 0
index = 0

while len(people) > 0:

    counter += 1

    if counter % people_skipped == 0:
        person_executed.append(people.pop(index))
    else:
        index += 1

    if index >= len(people):
        index = 0

print(str(person_executed).replace(' ', '').replace('\'', ''))
