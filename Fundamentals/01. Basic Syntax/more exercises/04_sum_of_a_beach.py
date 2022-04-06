word = input().lower()
counter = 0

if "sand" in word:
    if word.count("sand") > 1:
        word_counter = word.count("sand")
        counter += 1 * word_counter
    else:
        counter += 1
if "water" in word:
    if word.count("water") > 1:
        word_counter = word.count("water")
        counter += 1 * word_counter
    else:
        counter += 1
if "sun" in word:
    if word.count("sun") > 1:
        word_counter = word.count("sun")
        counter += 1 * word_counter
    else:
        counter += 1
if "fish" in word:
    if word.count("fish") > 1:
        word_counter = word.count("fish")
        counter += 1 * word_counter
    else:
        counter += 1

print(counter)
