def print_even_numbers(n):
    for i in range(2, n+1, 2):
        print(i)

n = int(input("Enter a positive integer: "))
print("Even numbers from 1 to", n)
print_even_numbers(n)