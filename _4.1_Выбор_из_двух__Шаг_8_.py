num1 = int(input())
num2 = int(input())
num3 = int(input())
d = num2 - num1  # ����� ������� ����� ���
f1 = num1 + d == num2  # ������� ����� 1
f2 = num2 + d == num3  #  ������� ����� 2
if f1 & f2:  # ���� ����������� ������� ����� 1 � ������� ����� 2, ����� ������� YES
    print('YES')
else:
    print('NO')
