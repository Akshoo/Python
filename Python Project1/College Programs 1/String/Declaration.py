a = 'String 1'
b = "String 2"
c = '''String 3'''
print("a = ", a , "\tb =  " , b , "\tc =  ", c)
print("a = ", type(a), "\tb =  ", type(b), "\tc =  ", type(c))
d = "All Boy's are Good"
e = "All Boy\'s are Good"
print("d = ",d , " ", "e = ", e)
print("d = ", type(d), "\te =  ", type(e))

# Printing of string 
print(a[0])     # S
print(a[1])     # t
print(a[2])     # r
print(a[3])     # i
print(a[4])     # n
print(a[5])     # g
print(a[6])     # 
print(a[7])     # 1

print(a[-0])    # S

print(a[-1])    # 1
print(a[-2])    # 
print(a[-3])    # g
print(a[-4])    # n
print(a[-5])    # i
print(a[-6])    # r
print(a[-7])    # t
print(a[-8])    # S

# Finding substring
print(a[0:6])   # String
print(a[2:6])   # ring
print(a[2:8])   # ring 1
print(a[0: ])   # String 1
print(a[ :8])   # String 1
print(a[-1: ])  # 1
print(a[ :-7])  # S 