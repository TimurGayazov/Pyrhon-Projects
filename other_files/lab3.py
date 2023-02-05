# (15,11)

number = input()
polinom = input()

n_mas = []
n_mas1 = []
n_mas2 = []
n_mas3 = []
p_mas = []

flag = 0
flag1 = 0

n_mas = list(number)
n_mas1 = list(number)
n_mas2 = n_mas
p_mas = list(polinom)

for i in range(0, 4):
    n_mas1.append('0')


#print(n_mas)
#print(n_mas1)
#print(p_mas)

while n_mas1[0] == '0':
    del n_mas1[0]


while (flag == 0):
    for i in range(0, len(p_mas)):
        if n_mas1[i] == p_mas[i]:
            n_mas1[i] = '0'
        else:
            n_mas1[i] = '1'
    while(n_mas1[0] == '0'):
        del n_mas1[0]
    if len(n_mas1) < 5:
        flag = 1

#print(n_mas1)
n_mas2 = n_mas + n_mas1
a2 = ''
for i in range(0, len(n_mas2)):
    a2 = a2+n_mas2[i]
print("Закодированная строка: ", a2)


# Декодирование с поиском ошибки
#print("Введите строку с ошибкой: ")
d_num = input('Введите строку с ошибкой или без: ')
n_mas3 = list(d_num)
n_mas4 = n_mas3.copy()
n_mas5 = n_mas3.copy()
#print(n_mas4)

while(flag1 == 0):
    for i in range(0, len(p_mas)):
        if n_mas3[i] == p_mas[i]:
            n_mas3[i] = '0'
        else:
            n_mas3[i] = '1'
    while(n_mas3[0] == '0'):
        if n_mas3 == ['0', '0', '0', '0']:
            print('Передача прошла без ошибок')
            break
        del n_mas3[0]
    if len(n_mas3) < 5:
        flag1 = 1

x0 = ['1']
x1 = ['1','0']
x2 = ['1','0','0']
x3 = ['1','0','0','0']
x4 = ['1','1']
x5 = ['1','1','0']
x6 = ['1','1','0','0']
x7 = ['1','1','0','1']
x8 = ['1','0','1']
x9 = ['1','0','1','0']
x10 = ['1','1','1']
x11 = ['1','1','1','0']
x12 = ['1','1','1','1']
x13 = ['1','1','0','1']
x14 = ['1','0','0','1']

x_mas = [x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14]


for i in range(0, len(x_mas)):
    if n_mas3 == x_mas[i]:
        n_mas4.reverse()
        n_mas4[i] = 'X'
        n_mas4.reverse()
        a3 = ''
        for j in range(0, len(n_mas4)):
            a3 = a3+n_mas4[j]
        print("Ошибка обнаружена в", i, "бите: ", a3)
        n_mas5.reverse()
        if n_mas5[i] == '0':
            n_mas5[i] = '1'
            n_mas5.reverse()
            a4 = ''
            for i in range(0, len(n_mas5)):
                a4 = a4 + n_mas5[i]
            print("Ошибка исправлена: ", a4)
        else:
            n_mas5[i] = '0'
            n_mas5.reverse()
            a5 = ''
            for i in range(0, len(n_mas5)):
                a5 = a5 + n_mas5[i]
            print("Ошибка исправлена: ", a5)


del n_mas5[-1]
del n_mas5[-1]
del n_mas5[-1]
del n_mas5[-1]

a = ''
for i in range(0, len(n_mas5)):
    a = a+n_mas5[i]


print("Декодированная строка: ", a)