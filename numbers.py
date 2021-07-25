# Numeric Data Types in Python
#integer(int) -withput point all +Ve and -Ve
#float  -number with point a;; +Ve and -Ve
#complex --imaginary number -i&j

x = 1 #int
y = 3.45 #float
z = 1j  #complex

print(x,y,z)
print(type(x))
print(type(y))
print(type(z))


#number can be converted from one form to another

#float to int
a = int(y)
print(a)

#float to complex
b = complex(y)
print(b)

#int to float
c = float(a)
print(c)

#int to complex
d = complex(x)
print(d)

#complex cannot be converted into float or int



#random number in python
#python doesnt have function to create random number but it has built-in module to create random number

import random
print(random.randrange(50,100))

#output can be: 50,51,52,.......,98,99
#to include 100, 101 should be endrange

#int or float can be casted into string by str() method

p = str(x)
q = str(y)
print(x)
print(y)
print(type(p))
print(type(q))
