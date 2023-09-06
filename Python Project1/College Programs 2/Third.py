# Predefined methods in Python.

# 1- Mathematical functions
import math
a, b, c, d = 9, 16, 25.5, 30.5
print(" Values : \n","*" * 9)
print("\ta = ", a, "\t\tb = ", b, "\tc = ", c, "\td = ", d)
print("\tsqrt(a) = ", math.sqrt(a), "\tsqrt(b) = ", math.sqrt(b)) 
print("\tceil(c) = ", math.ceil(c), "\tceil(d) = ", math.ceil(d))

print("\tfloor(c) = ", math.floor(c), "\tfloor(d) = ", math.floor(d))
print("\ttrunc(c) = ", math.trunc(c), "\ttrunc(d) = ", math.trunc(d))

print("\nTo Know Data-Type of the Variable : \n************************************")
print("type(a) = ", type(a), "\ttype(a) = ", type(b), "\ttype(c) = ", type(c), "\ttype(d) = ", type(d))
print("\nTo Know Address of the Variable : \n**********************************")
print("id(a) = ", id(a), "\tid(b) = ", id(b), "\tid(c) = ", id(c), "\t\tid(d) = ", id(d))