
#####Example of recursive function that counts
#### to 50 and back down
def recursiveFunction(n):
    if n > 50:
        print("******", n)
        return
    print(n)
    recursiveFunction(n+1)
    print("A", n)
    

recursiveFunction(1)

#####Example of factorial done with a 
#### iterative for loop
result = 5
for i in [4, 3, 2, 1]:
    result = result*i

print(result)



#####Example of doing factorial five using
##### multiple functions instead of recursion
#### used to show the stack and the amount of
#### n variables that would be on the stack
def stepFive(n):  
    return n 

def stepFour(n):
    return n * stepFive(n-1)

def stepThree(n):
    return n * stepFour(n-1)

def stepTwo(n):
    return n * stepThree(n-1)

def stepOne(n):
    return n * stepTwo(n-1)

n = 5
print(stepOne(n))


######
#### Doing the same factorial 5 with 
#### a single recursive function

def factorialFunction(n):

    if n == 1:
        return n
    x = factorialFunction(n-1)*n
   
    return x



x = 5
a = factorialFunction(x)
print(a)
