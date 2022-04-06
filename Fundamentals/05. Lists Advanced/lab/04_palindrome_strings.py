text_line = [item for item in input().split(" ")]
keyword = input()
palindrome_list = list()
counter = 0
for word in text_line:
    if word == keyword:
        counter += 1
    if word == word[::-1]:
        palindrome_list.append(word)

print(palindrome_list)
print(f"Found palindrome {counter} times")