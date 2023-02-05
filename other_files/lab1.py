a = 4
r = 0
ch = ''
print("Введите слово/предложение: ")
slovo = input()
mas = list(slovo)
kolvo = len(mas)
masiv = []
masiv1 = []
masiv2 = []
masiv3 = []
masiv4 = []


if kolvo > 16:
    print("Ошибка. Максимальное кол-во символов : 16.", "Вы ввели", kolvo, "символов.")

if kolvo < 16:
    for q in range(0, 16-kolvo):
        mas.append(" ")
    for i in range(a):
        masiv.append([])
        for j in range(a):
            masiv[i].append(mas[r])
            r = r+1
    #print(mas)
    #print(masiv)

#ввод ключа
print("Введите ключ по столбцам:")
stolb = input()
stolb_key = list(stolb)
print("Введите ключ по строкам:")
strok = input()
strok_key = list(strok)


st_key = [int(strok_key[0]), int(strok_key[1]),int(strok_key[2]),int(strok_key[3])]
sb_key = [int(stolb_key[0]), int(stolb_key[1]),int(stolb_key[2]),int(stolb_key[3])]

#print(sb_key)
#print(st_key)

#обнуление массива для перестановки таблицы по столбцам
for k in range(a):
    masiv1.append([])
    for l in range(a):
        masiv1[k].append(' ')

#print(masiv1)

#обеуление массива для перестановки таблицы по строкам
for k in range(a):
    masiv2.append([])
    for l in range(a):
        masiv2[k].append(' ')





#перестановка по столбцам
for x in range(0,4):
    for y in range(0,4):
        masiv1[x][sb_key[y]-1] = masiv[x][y]

#print(masiv1)

#перестановка по строкам
for x in range(0,4):
    for y in range(0,4):
        masiv2[st_key[x]-1][y] = masiv1[x][y]

#print(masiv2)

#Вывод закодированных символов
sim = '"'
for x in range(0,4):
    for y in range(0,4):
        sim = sim + masiv2[x][y]
sim = sim + '"'
print(sim)



print("\nВведите ключ по столбцам:")
stolb1 = input()
stolb_key1 = list(stolb1)
print("Введите ключ по строкам:")
strok1 = input()
strok_key1 = list(strok1)
sb_key1 = [int(stolb_key1[0]), int(stolb_key1[1]),int(stolb_key1[2]),int(stolb_key1[3])]
st_key1 = [int(strok_key1[0]), int(strok_key1[1]),int(strok_key1[2]),int(strok_key1[3])]


#пустые массивы для декодирования
for k in range(a):
    masiv3.append([])
    for l in range(a):
        masiv3[k].append(' ')

for k in range(a):
    masiv4.append([])
    for l in range(a):
        masiv4[k].append(' ')


#перестановка по строкам
for x in range(0,4):
    for y in range(0,4):
        masiv3[x][y] = masiv2[st_key1[x]-1][y]

#перестановка по столбцам
for x in range(0,4):
    for y in range(0,4):
        masiv4[x][y] = masiv3[x][sb_key1[y]-1]


#вывод декодированных символов
sim1 = '"'
for x in range(0,4):
    for y in range(0,4):
        sim1 = sim1 + masiv4[x][y]
sim1 = sim1 + '"'
print(sim1)