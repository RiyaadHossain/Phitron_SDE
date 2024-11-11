a,b = map(int,input().split())

def isLucky(num):
    return all(digit in '47' for digit in str(num))

ans = [num for num in range(a,b+1) if(isLucky(num))]

if len(ans):
    print(*ans)
else:
    print(-1)