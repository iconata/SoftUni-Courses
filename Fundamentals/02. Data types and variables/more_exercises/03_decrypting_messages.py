def cipher_character(character, shift):
    # Don't convert anything other than english characters
    if not character.isalpha():
        return character
    # declare some helping constants
    alpha_length = 26
    ascii_shift = ord('A') if character.isupper() else ord('a')
    cipher_shift = shift % alpha_length

    # shift down to 0..25 for a..z
    shifted = ord(character) - ascii_shift
    # rotate the letter and handle "wrap-around" for negatives and value >= 26
    shifted = (shifted + cipher_shift + alpha_length) % alpha_length
    # shift back up to english characters
    return chr(shifted + ascii_shift)

# Rotate a string k-positions
def cipher_string(string, shift):
    return ''.join(cipher_character(c, shift) for c in string)


shift = int(input())
lines = int(input())

for i in range(lines):
    letters = input()
    letters_as_list = [letters]

    print(cipher_string(letters_as_list, shift), end="")