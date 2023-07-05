# Write code for algorithm 1 below


def print_numbers(n):
    # Base case: Stop recursion when n reaches zero
    if n == 0:
        return

    # Print the current number
    print(n)

    # Recursive case: Call the function again with n-1
    print_numbers(n-1)


# Test the function
number = int(input("Enter a positive number: "))
print_numbers(number)
