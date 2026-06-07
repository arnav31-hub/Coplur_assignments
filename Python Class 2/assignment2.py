# 2) Input 2 strings concatenate them and store in another variable. then perform generally used string methods on it:

# Taking input of two strings:
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Concatenate two strings:
text = str1 + str2

print("\nConcatenated String:", text)

# Performing different string method on concatenated string:
print("lower():", text.lower())
print("upper():", text.upper())
print("title():", text.title())
print("swapcase():", text.swapcase())
print("capitalize():", text.capitalize())
print("casefold():", text.casefold())
print("center(10):", text.center(10))
print("count('a'):", text.count('a'))
print("endswith('a'):", text.endswith('a'))
print("find('a'):", text.find('a'))
print("isalnum():", text.isalnum())
print("isdigit():", text.isdigit())
print("isnumeric():", text.isnumeric())
print("isspace():", text.isspace())
print("replace('', 'A'):", text.replace('a', ''))
