# 1-> Content Test's
s = "Aman"
print(s.isalpha())      # True
print(s.isdigit())      # False
print(s.isalnum())      # True
print(s.islower())      # False
print(s.isupper())      # False
print(s.startswith('A'))    # True
print(s.endswith('n'))      # True

print("\n")
s = "My name is Aman005"
print(s.isalpha())      # false
print(s.isdigit())      # False
print(s.isalnum())      # False
print(s.islower())      # False
print(s.isupper())      # False
print(s.startswith('A'))    # False
print(s.endswith('n'))      # False

# 2 -> Search and Replace
m = "Akhil"
print(m.find('l'))      # 4
print(m.replace('h',' '))   # Ak il
n = "      Hello       "
print(m.lstrip())
print(m.rstrip())
print(m.strip())


# 3 -> Split and Partition
o = "Python Strings"
print(o.split())    # ['Python', 'Strings']
