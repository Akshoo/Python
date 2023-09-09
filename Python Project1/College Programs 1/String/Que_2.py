''' Input a string  and print length of the string '''
s1 = input("Enter a string : ")
print("String s1 length = ", len(s1))

# Check if the string contains only alphanumeric characters
if s1.isalpha():
    print("String s1 =", s1)
else:
    print("Enter a string without using any digit value.")
# && s1 != s1.isdigit()