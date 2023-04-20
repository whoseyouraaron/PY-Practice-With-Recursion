# Write code for algorithm 5 below
def is_palindrome(str):
    if len(str) == 1 or len(str) == 0:
        return True

    else:
        return (str[0] == str[-1]) and is_palindrome(str[1:-1])

print("is 'banana' a palindrome?")
print(is_palindrome('banana'))
print("is 'racecar' a palindome?")
print(is_palindrome('racecar'))