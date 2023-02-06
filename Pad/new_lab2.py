import numpy as np
import sys
import os
import random

def hidden_func(mat_copy, mat): # функция которая записывает исходные и конечные данные в txt файл
    np.savetxt("lab2_1.txt", mat_copy, fmt='%.1d')
    np.savetxt("lab2_2.txt", mat, fmt='%.1d')
    open("result_lab2.txt", "w").write(open("lab2_1.txt", "r").read() + "\n" + open("lab2_2.txt", "r").read())
    os.remove("lab2_1.txt")
    os.remove("lab2_2.txt")



def main_func(mat, m, n): # функция поиска среднего значения каждого столбца и строчки
    print(mat)
    print(" ")
    mat_copy = mat
    list = []
    list1 = []

    # print("-----")
    for i in range(0, m):
        # print(*mat[i], "---", sum(mat[i]) // m)
        list1.append([sum(mat[i]) // m])
    # print("-----")

    new_row = np.array(list)
    for i in range(0, n):
        # print(*mat[:, i], "---", sum(mat[:, i]) // n)
        list.append(sum(mat[:, i]) // n)
    list1.append([sum(list) // len(list)])
    new_row = np.array(list)
    mat = np.vstack([mat, new_row])
    mat = np.c_[mat, list1[:]]
    # print(new_row, "строка")
    print("Результат матрица вида: ", m+1,"X",n+1)
    print(mat)
    hidden_func(mat_copy, mat)




while True: # рандоманая генерация матрицы
    check = int(input("Введите 1 для автоматического заполнения матрицы: "))
    if check == 1:
        m = random.randint(2, 10)  # столбец
        n = random.randint(2, 10)  # строка
        mat = np.random.randint(0, 20, (m, n))  # столбец, строка
        print("Матрица вида:", m, "X", n)
        main_func(mat, m, n)
    else:
        print("Ощибка ввода")
        sys.exit()