"""A student wants to swap a = 5 and b = 10 so that a becomes 10 and b becomes 5. They write: a = b; b = a. Explain the bug. write the correct solution"""
a = 5
b = 10

a,b = b,a
print (a,b )
