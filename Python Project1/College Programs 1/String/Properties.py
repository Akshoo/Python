# 1 -> Python's string are immutable.
s = "Hello"
print(s)
print(id(s))
# s[0] = 'm'  # TypeError: 'str' object does not support item assignment
s = "by"
print(s)
print(id(s))
e = "by"
print(s)
print(id(s))

# 2 -> Strings can be concatenated by using '+' operator.
ns1 = s + " Ajay"
print(ns1)      # by Ajay
v = " Vishwakarma"
ns2 = ns1 + v
print(ns2)      # by Ajay Vishwakarma

# 3 -> Strings can be replicated during printing.
print('@' * 10)     # @@@@@@@@@@
print("*" * 20)     # ********************

# 4 -> We can find wheather one string is a part of another by---
print('b' in s)     # True
print('s' in s)     # False
print(' ' in s)     # False

# 5 -> we can find length of tbe string by using---
print("Length of ns1 = ",len(ns1))      # 7
print("Length of ns2 = ",len(ns2))      # 19