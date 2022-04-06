searched_word = input()
substring = input()

while searched_word in substring:
    substring = substring.replace(searched_word, '')

print(substring)
