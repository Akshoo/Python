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
t = "My name is Aman005"
print(t.isalpha())      # False
print(t.isdigit())      # False
print(t.isalnum())      # False
print(t.islower())      # False
print(t.isupper())      # False
print(t.startswith('A'))    # False
print(t.endswith('n'))      # False

# 2 -> Search and Replace
m = "Akhil"
print(m.find('l'))      # 4
print(m.replace('h',' '))   # Ak il
n = "      Hello       "
print(n.lstrip())       # Hello
print(n.rstrip())       #       Hello
print(n.strip())        # Hello


# 3 -> Split [returns list] and Partition [returns tuple]
o = "Python Strings"
print(o.split())    # ['Python', 'Strings']
p = "My name is - Ajay"
print(p.split('-'))     # ['My name is ', ' Ajay']
q = "One-Two-Three-Four"
print(q.split('-'))                     # ['One', 'Two', 'Three', 'Four']
print(q.split('-' , maxsplit = 1))      # ['One', 'Two-Three-Four']  
print(q.split('-' , maxsplit = 2))      # ['One', 'Two', 'Three-Four']
print(q.split('-' , maxsplit = 5))      # ['One', 'Two', 'Three', 'Four']
r = "I could eat apples everday"
print(r.partition("apples"))            # ('I could eat ', 'apples', ' everday')

# 4 -> Other Methods of string
print(s.upper())        # AMAN
print(s.lower())        # aman
result = '-'.join(s)
print(result)           # A-m-a-n
u = "myself Ajay vishwakarma"
print(u.capitalize())   # Myself ajay vishwakarma
print(u.title())        # Myself Ajay Vishwakarma
print(u.swapcase())     # MYSELF aJAY VISHWAKARMA
