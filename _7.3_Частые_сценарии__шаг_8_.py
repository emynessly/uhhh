summ = 0
n = int(input())
for i in range(n):
    if ((i**2)%10==2) or ((i**2)%10==5) or ((i**2)%10==8):
        summ = summ + i
print(summ)
