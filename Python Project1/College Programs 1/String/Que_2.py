s = "Bamboozled"
print(s[0:2])   # Ba
print(s[8:10])  # ed
print(s[2:])    # mboozled
print(s[0:6])   # Bamboo
print(s)        # Bamboozled
print(s[0]+s[2]+s[4]+s[6]+s[8])     # Bmoze
print(s[0]+s[3]+s[6]+s[9])          # Bbzd
print(s[0]+s[5]+s[8])               # Boe
print(s[0:6]+"Manager")             # BambooManger

t = "Bring It On"
print(t.upper())        # BRING IT ON
print(t.lower())        # bring it on
print(t.capitalize())   # Bring it on
print(t.title())        # Bring It On
print(t.swapcase())     # bRING iT oN
print(t.replace("It","Him"))  # Bring Him On

msg = "Keep Yourself Warm"
print(msg.partition(' '))   # ('Keep', ' ', 'Yourself Warm')
print(msg.split(' '))       # ['Keep', 'Yourself', 'Warm']
print(msg.swapcase())       # kEEP yOURSELF wARM
print(msg.count('e'))       # 3
print(len(msg))             # 18
print(msg[-1])              # m
print(msg[:1])              # k
print(msg[-1:3])            #
print(msg[:-3])             # Keep Yourself W
print(msg[-3:])             # arm
print(msg[0:2])             # ke
