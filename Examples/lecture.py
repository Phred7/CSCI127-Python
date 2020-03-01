import random

"""Example 1 code"""
a = 0
while (a != 5):
    a = random.randint(0, 10)
    print('a =', a)
print('finished')

"""Example 2 code"""
a = 5
while (a != 5):
    a = random.randint(0, 10)
    print('a =', a)
print('finished')

"""Example 3 code"""
for i in range(0, 10):
    print('i =', i)

"""Example 4 code"""
names = ["Jon", "Riley"]

for name in names:
    print('name =', name)

"""Example 5 code"""
name = "Jon"
for c in name:
    print('c =', c)

"""Example 6"""
num_list = [1, 2, 3]
char_list = ['a', 'b', 'c']

for number in num_list:
    for letter in char_list:
        print(number, letter)

"""Example 7"""
for i in range(0, 10):
    if i % 2 == 0:
        continue
    print(i)

"""Example 8"""
for i in range(0, 10):
    if i == 5:
        break
    print(i)