a, b = map(int, input().split())

def isLucky(num):
    f = True
    while num:
        curr = num%10
        num//=10
        if(curr != 4 and curr != 7):
            f=False
    return f

hasLucky = False
for i in range(a,b+1):
    if(isLucky(i)):
        print(i,end=" ")
        hasLucky = True

if hasLucky == False:
    print(-1)