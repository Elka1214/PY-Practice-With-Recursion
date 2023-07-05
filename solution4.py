# Write code for algorithm 4 below

def a_to_b(a, b):
    if b < 1:
        print("Invalid input")
    elif b == 0:
        return 1
    else:
        return a * a_to_b(a, b - 1)


print("2^4:")
print(a_to_b(2, 4))
