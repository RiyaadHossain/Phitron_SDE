n = input()
arr = list(map(int, input().split()))

mnIdx = arr.index(min(arr))
mxIdx = arr.index(max(arr))

arr[mnIdx], arr[mxIdx] = arr[mxIdx], arr[mnIdx]

print(*arr)