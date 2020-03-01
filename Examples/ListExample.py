

grade1 = 76
grade2 = 86

grades = [76, 86, 91, 86, 54, 32, 100]

names = ["test one", "hw 1", "hw2", "hw 3", "hw4", "exam2", "Final"]

for i in range(len(grades)):
    print(names[i] + ":\t " + str(grades[i]))


average = 0
for i in grades:
    average += i
print(average/len(grades))

average = 0
for i in grades:
    i = i + 5
    average += i

print(average/len(grades))
print(grades)

average = 0
for i in range(len(grades)):
    grades[i] += 5
    average += grades[i]

print(average/len(grades))
print(grades)







