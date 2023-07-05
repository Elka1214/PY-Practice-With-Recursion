# Write code for algorithm 5 below

def is_palindrome(string):
    if len(string) <= 1:
        return True
    else:
        return string[0] == string[-1] and is_palindrome(string[1:-1])


# Test the function
print("Is 'apple' a palindrome?")
print(is_palindrome('apple'))

print("Is 'tacocat' a palindrome?")
print(is_palindrome('tacocat'))
