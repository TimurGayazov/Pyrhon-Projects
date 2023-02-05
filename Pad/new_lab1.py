import random
import sys

while True:
    mas = []

    check_method = int(input("Введите 0 или 1 для реализации алгоритма с использованием стандартных функций или без: "))
    check = int(input("Введите 0 или 1 для ручного или автоматического заполнения списка: "))


    def manual_filling():
        count_elem = int(input("Введите количество элементов списка: "))

        for i in range(count_elem):
            mas.append(int(input()))
        print(mas)
        mas.append(999)


    def manual_filling_wo_func(mas):
        count_elem = int(input("Введите количество элементов списка: "))
        for i in range(0, count_elem):
            mas+=[int(input())]
        print(mas)
        mas+=[int(999)]

    min_row_id = 0
    def main_func(mas):
        min_row = 999
        min_row_id = 0
        k = 0
        for i in range(0, len(mas)):
            if (mas[i] %2 == 0):
                if (mas[i] < min_row and mas[i] != min_row):
                    min_row = mas[i]
                    min_row_id = i
                    # print(min_row)
                k+=1

            elif (mas[i] %2 != 0 and k > 0) or i == len(mas):
                mas[min_row_id] = " "
                min_row_id = 0
                min_row = 999
                k = 0

            if i == len(mas) and mas[i] %2 == 0:
                mas[min_row_id] = " "
                min_row_id = 0
                min_row = 999
                k = 0
        del mas[-1]
        ii = 0
        while " " in mas:
            if mas[ii] == " ":
                del mas[ii]
            ii+=1

        print(mas)
        print(" ")


    def with_func(mas):
        if check == 0:
            if check_method == 0:
                manual_filling()
                main_func(mas)
            elif check_method == 1:
                manual_filling_wo_func(mas)
                main_func(mas)


        elif check == 1:
            if check_method == 0:
                mas = [random.randint(0, 100) for i in range(random.randint(5, 10))]
                print(mas)
                mas.append(999)
            elif check_method == 1:
                mas = [random.randint(0, 100) for i in range(random.randint(5, 10))]
                print(mas)
                mas+=[int(999)]
            main_func(mas)
        else:
            print("Ошибка ввода")
            sys.exit()


    if check_method == 0: with_func(mas)
    elif check_method == 1: with_func(mas)
    else: print("Введите только 0 или 1")


