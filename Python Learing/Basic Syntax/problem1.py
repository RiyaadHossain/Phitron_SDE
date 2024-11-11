num = input().strip()

reversed_num = int(num[::-1])

palin_check = num == str(reversed_num)

print(reversed_num)
if(palin_check):
    print("YES")
else:
    print("NO")



