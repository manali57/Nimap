n = int(input())
if(n <= 0):
    print("invalid input")
else:
    x= input().split()
    y=sorted(x,key = len)
    print(x)
    print(y)