def calculate_average(numbers):
    if not numbers:
        return None
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage:
num_list = [float(x) for x in input("Enter numbers separated by space: ").split()]
avg = calculate_average(num_list)
if avg is not None:
    print("Average:", avg)
else:
    print("No numbers provided to calculate average.")