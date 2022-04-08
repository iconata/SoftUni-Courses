def palindrome_number(nums):
    for x in nums:
        if x == x[::-1]:
            print("True")
        else:
            print("False")


numbers = input().split(", ")
palindrome_number(numbers)
