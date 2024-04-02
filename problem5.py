def calculate_square_root(n):
    return n ** 0.5

num = float(input("Enter a number: "))
if num >= 0:
    sqrt = calculate_square_root(num)
    print("Square root of", num, "is", sqrt)
else:
    print("Invalid input. Please enter a non-negative number.")
