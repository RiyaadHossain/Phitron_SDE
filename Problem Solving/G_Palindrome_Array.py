n = int(input())
arr = list(map(int, input().split()))

revArr = arr[::-1]

if arr == revArr:
    print("YES")
else:
    print("NO")
