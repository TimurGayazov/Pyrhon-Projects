# mas = [1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 7]
# mas_index = []
# print(mas)
#
# for i in range(0, len(mas)):
#     mas_index.append(mas.count(mas[i]))
#
# print(mas_index)
#
# for i in range(0, len(mas_index)):
#     if mas_index[i] == 1:
#         mas[i] = " "
#
#
#
# print(mas)

mas = [1, 2, 3, 3, 2, 4, 5, 5, 9]
mas_index = []
print(mas)

def main_f(mas):
    mas_index = []
    k = 0
    for i in range(0,len(mas)):
        for j in range(0, len(mas)):
            if mas[i] == mas[j]:
                k+=1
        mas_index+=[int(k)]
        k=0

    for i in range(0, len(mas_index)):
        if mas_index[i] == 1:
            mas[i] = " "
    print(mas_index)
    print(mas)

main_f(mas)

# for i in range(0, len(mas)):
