password = input()
length_valid = True
at_least_two_digits = True
no_symbols = True
digits_counter = 0

for char in password:
    if not char.isalnum():
        no_symbols = False
    if char.isdigit():
        digits_counter += 1
    if sum(map(str.isdigit, password)) < 2:
        at_least_two_digits = False
    if 6 <= len(password) <= 10:
        length_valid = True
    else:
        length_valid = False

if length_valid and at_least_two_digits and no_symbols:
    print("Password is valid")
else:
    if not length_valid:
        print("Password must be between 6 and 10 characters")
    if not no_symbols:
        print(f"Password must consist only of letters and digits")
    if not at_least_two_digits:
        print(f"Password must have at least 2 digits")
