s = input()

cnt = 0
track = []

for c in s:
    if c=='L': 
        cnt+=1
    elif cnt: 
        track.append(cnt)
        cnt = 0

print(len(track))
for i in track:
    for j in range(0, i):
        print('L', end="")
    for j in range(0, i):
        print('R', end="")
    print()
    