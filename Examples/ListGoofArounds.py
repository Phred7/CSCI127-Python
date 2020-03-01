

grades = [76, 86] #, 91, 86, 54, 32, 100]

grades = grades * 6

print(grades)

histogram = [5, 4, 6, 8, 2]


for i in histogram:
    for j in range(i):
        print("*", end="")

    print("")   

for i in histogram:
    print(i * "*")
