num = input()
revNum = str(int(num[::-1]))

print(revNum)
if num == revNum:
    print("YES")
else:
    print("NO")