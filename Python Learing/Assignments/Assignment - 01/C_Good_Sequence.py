from collections import Counter

n  = int(input())
arr = list(map(int, input().split()))


freq = Counter(arr)

ans  = 0
for key,val in freq.items():
    if(key > val): ans += val
    else: ans+= (val-key)

print(ans)