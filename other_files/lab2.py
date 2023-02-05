# Здаание А

number = input()


mas = list(number)
dlina = len(mas)
qwerty = 0

a = mas.reverse()
#print(a)
for i in range(0,dlina):
    mas[i] = mas[i].replace('a','10',1)
    mas[i] = mas[i].replace('A','10',1)
    mas[i] = mas[i].replace('b','11',1)
    mas[i] = mas[i].replace('B','11',1)
    mas[i] = mas[i].replace('c','12',1)
    mas[i] = mas[i].replace('C','12',1)
    mas[i] = mas[i].replace('d','13',1)
    mas[i] = mas[i].replace('D','13',1)
    mas[i] = mas[i].replace('e','14',1)
    mas[i] = mas[i].replace('E','14',1)
    mas[i] = mas[i].replace('f','15',1)
    mas[i] = mas[i].replace('F','15',1)


for i in range(0,dlina):
    mas[i] = int(mas[i])


for i in range(0,dlina):
    qwerty = qwerty + (16**i * mas[i])

print(qwerty)



# Задание B

number1 = (-12003.21345)


qwerty = bin(12003)
qwerty1 = bin(21345)
mas1 = list(qwerty)
mas2 = list(qwerty1)

#123

del mas1[0]
del mas1[0]
del mas2[0]
del mas2[0]
mas2.insert(0,'.')

#print(mas1)
#print(mas2)

if number1>0:
    mas1.insert(0,'0')

if number1<0:
    mas1.insert(0,'1')

for i in range(0,len(mas2)):
    mas1.append(mas2[i])



#print(number1)
#print(mas1)



for i in range(0,len(mas1)):
    if mas1[i] == '.':
        m_n = i

m_n1 = 1

exp = 14 + ((2**10) - 1)
exp1 = bin(exp)
exp_mas = list(exp1)

del exp_mas[0]
del exp_mas[0]

del mas1[15]
mas1.insert(1,'.')

#print(mas1)
mas4 = mas1
del mas4[1]
del mas4[0]

#print(m_n)

#print(exp_mas)

result = [mas1[0]]
for i in range(0,len(exp_mas)):
    result.append(exp_mas[i])

for i in range(0,len(mas4)):
    result.append(mas4[i])



#result = mas1[0] + exp_mas + mas4

print(result)