''' Demonstrate how to create simple and multiline string in python and wheather a string can changed  after creation?
    Also show the usage of len() , min() and max() functions in python. '''

simple_string = "Hello, World!"

multiline_string = """
This is a multiline string.
It can span across multiple lines.
"""
# String Immutability:
original_string = "Hello"
modified_string = original_string + ", World!"
print(modified_string)       # Output: "Hello, World!"

# Usage of len(), min(), and max() functions:
text = "Python"
length = len(text)      
print("Length of the string:", length)       # Output: 6
text = "abcABC123"
smallest_char = min(text)
print("Smallest character:", smallest_char)  # Output: "1"
text = "abcABC123"
largest_char = max(text)
print("Largest character:", largest_char)    # Output: "c"
