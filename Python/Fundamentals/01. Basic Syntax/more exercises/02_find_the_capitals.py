def find_capitals(word):
    index_list = list()
    for index, value in enumerate(word):
        if value.isupper():
            index_list.append(index)
    return index_list


print(find_capitals(word=input()))
