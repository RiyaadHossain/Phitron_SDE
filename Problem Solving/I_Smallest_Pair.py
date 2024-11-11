t = int(input())

while t:

    n = int(input())
    arr = list(map(int, input().split()))

    ans = 1e9
    for j in range(1, n):
        for i in range(j):
            ans = min(ans, arr[i]+arr[j]+j-i)

    print(ans)

    t-=1
