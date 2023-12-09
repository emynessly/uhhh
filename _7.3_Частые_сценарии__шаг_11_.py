r = 0
n = int(input())
for i in range(10000000):
    if n%(i+1)==0:
        r = r + (i+1)
print(r)
