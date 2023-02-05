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


    # def automatic_filling():
    #     mas = [random.randint(0, 100) for i in range(random.randint(5, 30))]
    #     print(mas)



    min_row_id = 0
    def main_func(mas): # с функциями
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

    def main_wo_func(mas): # без функций
        min_row = 999
        min_row_id = 0
        k = 0
        for i in range(0, len(mas)):
            if (mas[i] % 2 == 0):
                if (mas[i] < min_row and mas[i] != min_row):
                    min_row = mas[i]
                    min_row_id = i
                    # print(min_row)
                k += 1

            elif (mas[i] % 2 != 0 and k > 0) or i == len(mas):
                mas[min_row_id] = " "
                min_row_id = 0
                min_row = 999
                k = 0

            if i == len(mas) and mas[i] % 2 == 0:
                mas[min_row_id] = " "
                min_row_id = 0
                min_row = 999
                k = 0
        del mas[-1]
        ii = 0
        while " " in mas:
            if mas[ii] == " ":
                del mas[ii]
            ii += 1

        print(mas)
        print(" ")




    def without_func(mas):
        if check == 0:
            manual_filling()

            main_wo_func(mas)
        elif check == 1:
            # automatic_filling()
            mas = [random.randint(0, 100) for i in range(random.randint(5, 10))]

            print(mas)

            mas.append(999)
            main_wo_func(mas)
        else:
            print("Ошибка ввода")
            sys.exit()

    def with_func(mas):
        if check == 0:
            manual_filling()
            main_func(mas)

            # main_func(mas)
        elif check == 1:
            # automatic_filling()
            mas = [random.randint(0, 100) for i in range(random.randint(5, 10))]

            print(mas)
            mas.append(999)
            main_func(mas)
        else:
            print("Ошибка ввода")
            sys.exit()

#
    if check_method == 0:
        with_func(mas)
    elif check_method == 1:
        without_func(mas)
    else: print("Введите только 0 или 1")


