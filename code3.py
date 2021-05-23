n = int(input())
sumOfArr = 0
multiOfArr = 1
arr= []
def checkPrime(num):
    if num > 1:  
        for i in range(2,num):  
            if (num % i) == 0:  
                return False
        else:  
            return True
if(n < 10):
    print('Invalid Number')
elif(checkPrime(n)):
    print('Enter a different number')
else:
    for i in range(1, n + 1):
        if n % i == 0:
            if i % 2 == 0:
                arr.append(i)
                sumOfArr += i
                multiOfArr *= i
    print(sorted(arr,reverse =True))
    print(sumOfArr)
    print(multiOfArr)