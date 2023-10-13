n = int(input())
m = n//1000
r = (n%1000)//100
k = (n%100)//10
l = n%10
print('The digit in the thousands position is', m)
print('The digit in the hundreds position is', r)
print('The digit in the tens position is', k)
print('The digit in the units position is', l)
