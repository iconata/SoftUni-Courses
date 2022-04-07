numbers = [x for x in input().split()]
text = [i for i in input()]
sum_of_digits = 0
secret_word = ''

for nums in numbers:
    sum_of_digits = 0

    for n in nums:
        sum_of_digits += int(n)
    
    if len(text) > sum_of_digits:
        index = sum_of_digits
        secret_word += text[index]
        text.pop(index)
    else:
        index = (sum_of_digits - len(text))
        secret_word += text[index]
        text.pop(index)

print(secret_word)
