# Write code for algorithm 3 below

def fibonacci(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        prev_prev = 0
        prev = 1
        for _ in range(3, n + 1):
            current = prev_prev + prev
            prev_prev = prev
            prev = current
        return prev


# Test the function
n = int(input("Enter the value of n: "))
result = fibonacci(n)
if result is not None:
    print(f"The {n}th element in the Fibonacci sequence is: {result}")
else:
    print("Invalid input! n should be a positive integer.")
