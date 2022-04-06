def chars_in_range(ch1, ch2):
    chars = list()
    for i in range(ord(ch1) + 1, ord(ch2)):
        chars.append(chr(i))
    print(" ".join(chars))


chars_in_range(ch1=input(), ch2=input())


def chars_in_range(ch1, ch2):
    for i in range(ord(ch1) + 1, ord(ch2)):
        print(chr(i), end=" ")


chars_in_range(ch1=input(), ch2=input())
