n = int(input())

arr = list(map(int, input().split()))

ans = 1e9
for i in arr[::1]:
    cnt = 0
    while i%2 == 0:
        i//=2
        cnt+=1
    ans = min(ans, cnt)

print(ans)