
def reverseString(inputString):
    outputString = ""
    for i in range(len(inputString), 0 , -1):
        outputString = outputString + inputString[i-1]
    return outputString

def findLargest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b        
    else:
        return c
    
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def fibonacci(n):
    sequence = [None] * n
    for i in range(len(sequence)):
        if i == 0 or i == 1:
            sequence[i] = 1
        else:
            sequence[i] = sequence[i-1] + sequence[i-2]
    return sequence[n-1]
        
print(reverseString("string"))
print(findLargest(3,2,1))
print(factorial(3))
print(fibonacci(5))