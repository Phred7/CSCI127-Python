import random



def takeAverage(alist):
    average = 0
    for i in alist:
        average += i
    return (average/len(alist))



def main():
    myList = []
    for i in range(100):
        num = random.randint(0, 1000)
        myList.append(num)
    print(takeAverage(myList)
)    

main()
