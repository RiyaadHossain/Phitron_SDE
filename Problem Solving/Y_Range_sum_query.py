n,q = map(int, input().split())

arr = list(map(int, input().split()))

pref = [0]*(n+1)
for i in range(1, n+1):
    pref[i] = pref[i-1] + arr[i-1]

for _ in range(q):
    l,r = map(int, input().split())
    print(pref[r] - pref[l-1])
