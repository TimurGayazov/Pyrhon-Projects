import numpy as np
import sys
import random

def main_func(mat, m, n):
    print(mat)
    list = []
    list1 = []

    for i in range(0, m):
        print(*mat[i], "---", sum(mat[i]) // m)
        list1.append([sum(mat[i]) // m])

    print("-----")
    # new_array = np.append(mat, [list1], axis=1)
    # mat = np.insert(mat, 2, list1, axis=1)
    mat = np.append(mat, list1, axis=1)

    print(list1, "столбец")
    # new_row = np.array(list)
    for i in range(0, n):
        print(*mat[:,i], "---", sum(mat[:,i]) // n)
        list.append(sum(mat[:,i]) // n)

    
    new_row = np.array(list)
    mat = np.vstack([mat, new_row])
    print(new_row, "строка")
    print(mat)


while True:
    check = int(input("Введите 1 для автоматического заполнения матрицы: "))
    if check == 1:
        print("Автоматическое заполнение")
        # m = random.randint(2, 10)  # столбец
        # n = random.randint(2, 10)  # строка
        m = 3
        n = 3
        mat = np.random.randint(0, 20, (m, n))  # столбец, строка
        print("Матрица вида:", m, "X", n)
        main_func(mat, m, n)
    else:
        print("Ощибка ввода")
        sys.exit()