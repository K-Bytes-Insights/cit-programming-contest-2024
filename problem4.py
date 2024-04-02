def is_palindrome(s):
    s = s.lower()  # Convert to lowercase for case insensitivity
    return s == s[::-1]  # Compare string with its reverse

string = input("Enter a string: ")
if is_palindrome(string):
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")
