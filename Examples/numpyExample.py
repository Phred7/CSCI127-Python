import numpy as np
import random

#One
v = np.random.randint(0, 101, 10)

print(v)

##print("[", end="")
##for i in range(1, 10, 2):
##    print(v[i], end="")
##print("]")

#2
print(v[1::2])
#Three
print(v[::-1])
#Four
a = np.array([1, 2, 3, 4, 5])
b = a[1:4]
b[0] = 200
print(b)
print(a[1])
c = np.copy(a)
c[0] = 500
print(a)
print(c)

#Five
m = np.random.randint(0, 101, [5,5])
print("2D Array")
print(m)

#Grabbing one element from 2d array
print(m[2] [3])

#Six
print("Rows in Reverse")
n = m[::, ::-1 ]
print(n)

#Seven
print("Rows are in reverse order")
n = m[::, ::]
print(n)
#Eight
print("Rows are in reverse order")
n = m[::-1, ::-1]
print(n)
#Nine
print("Cut off the first and last rows and columns")

n = m[1:4, 1:4]
print(n)


