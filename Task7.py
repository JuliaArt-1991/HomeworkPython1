# Доп. задача 6
n = input('Введите шестизначных номер билета: ')
n1 = int(n[0])+int(n[1])+int(n[2])
n2 = int(n[3])+int(n[4])+int(n[5])
if n1 == n2:
    print('Yes')
else:
    print('No')