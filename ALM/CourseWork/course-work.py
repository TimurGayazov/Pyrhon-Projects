from matrix import *

YArr = ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
s_line = '-' * 30


def matrix():
    pass


def check_state(XArr, state, count):
    if count == 1:
        count -= 1
        graph_scheme(XArr, state, count)
    if count == 0:
        print(f'{s_line}\nLooping...')
        exit()


def graph_scheme(XArr, state, count):
    # --S0--
    if state == 'S0':
        # S0 -> S1
        if ((XArr[1] == '0' and XArr[2] == '1' and XArr[3] == '0' and XArr[4] == '0' and XArr[5] == '0') or
                (XArr[1] == '0' and XArr[2] == '0' and XArr[4] == '0' and XArr[5] == '0')):
            YArr[1] = 1
            YArr[2] = 1
            YArr[3] = 1
            print(f'S0 -> {" ".join(map(str, YArr))} -> S1')
            state = 'S1'
            YArr[1] = 0
            YArr[2] = 0
            YArr[3] = 0

        # S0 -> S2
        elif ((XArr[1] == '0' and XArr[2] == '1' and XArr[3] == '0' and XArr[4] == '0' and XArr[5] == '1') or
              (XArr[1] == '0' and XArr[2] == '0' and XArr[4] == '0' and XArr[5] == '1')):
            print(f'S0 -> {" ".join(map(str, YArr))} -> S2')
            state = 'S2'

        # S0 -> S4
        elif XArr[1] == '1' and XArr[12] == '0':
            YArr[5] = 1
            YArr[6] = 1
            YArr[7] = 1
            print(f'S0 -> {" ".join(map(str, YArr))} -> S4')
            state = 'S4'
            YArr[5] = 0
            YArr[6] = 0
            YArr[7] = 0

        # S0 -> S5
        elif XArr[1] == '1' and XArr[12] == '1' and XArr[13] == '1':
            YArr[16] = 1
            YArr[17] = 1
            YArr[18] = 1
            print(f'S0 -> {" ".join(map(str, YArr))} -> S5')
            state = 'S5'
            YArr[16] = 0
            YArr[17] = 0
            YArr[18] = 0
        # S0 -> S6
        elif ((XArr[1] == '0' and XArr[2] == '1' and XArr[3] == '1') or
              (XArr[1] == '0' and XArr[2] == '1' and XArr[3] == '0' and XArr[4] == '1' and XArr[6] == '1') or
              (XArr[1] == '0' and XArr[2] == '0' and XArr[4] == '1' and XArr[6] == '1')):
            print(f'S0 -> {" ".join(map(str, YArr))} -> S6')
            state = 'S6'

        # S0 -> S7
        elif XArr[1] == '1' and XArr[12] == '1' and XArr[13] == '0':
            YArr[1] = 1
            YArr[2] = 1
            YArr[15] = 1
            print(f'S0 -> {" ".join(map(str, YArr))} -> S7')
            state = 'S7'
            YArr[1] = 0
            YArr[2] = 0
            YArr[15] = 0

    # --S1--
    if state == 'S1':
        # S1 -> S1
        if XArr[9] == '0':
            print(f'S1 -> {" ".join(map(str, YArr))} -> S1\nLooping...\n{s_line}')
            exit()
        # S1 -> S2
        elif XArr[9] == '1':
            YArr[4] = 1
            print(f'S1 -> {" ".join(map(str, YArr))} -> S2')
            state = 'S2'
            YArr[4] = 0

    # --S2--
    if state == 'S2':
        # S2 -> S3
        if XArr[10] == '1' and XArr[11] == '1' and XArr[7] == '1':
            YArr[5] = 1
            YArr[7] = 1
            YArr[8] = 1
            YArr[9] = 1
            print(f'S2 -> {" ".join(map(str, YArr))} -> S3')
            state = 'S3'
            YArr[5] = 0
            YArr[7] = 0
            YArr[8] = 0
            YArr[9] = 0

        # S2 -> S4
        elif ((XArr[10] == '0' and XArr[12] == '0') or
              (XArr[10] == '1' and XArr[11] == '0') or
              (XArr[10] == '1' and XArr[11] == '1' and XArr[7] == '0')):
            YArr[5] = 1
            YArr[6] = 1
            YArr[7] = 1
            print(f'S2 -> {" ".join(map(str, YArr))} -> S4')
            state = 'S4'
            YArr[5] = 0
            YArr[6] = 0
            YArr[7] = 0

        # S2 -> S5
        elif XArr[10] == '0' and XArr[12] == '1' and XArr[13] == '1':
            YArr[16] = 1
            YArr[17] = 1
            YArr[18] = 1
            print(f'S2 -> {" ".join(map(str, YArr))} -> S5')
            state = 'S5'
            YArr[16] = 0
            YArr[17] = 0
            YArr[18] = 0

        # S2 -> S7
        elif XArr[10] == '0' and XArr[12] == '1' and XArr[13] == '0' and XArr[1] == '1':
            YArr[1] = 1
            YArr[2] = 1
            YArr[15] = 1
            print(f'S2 -> {" ".join(map(str, YArr))} -> S7')
            state = 'S7'
            YArr[1] = 0
            YArr[2] = 0
            YArr[15] = 0

        # S2 -> S8
        elif XArr[10] == '0' and XArr[12] == '1' and XArr[13] == '0' and XArr[1] == '0':
            YArr[21] = 1
            print(f'S2 -> {" ".join(map(str, YArr))} -> S8')
            state = 'S8'
            YArr[21] = 0

    # --S3--
    if state == 'S3':
        # S3 -> S3
        if XArr[14] == '0':
            print(f'S3 -> {" ".join(map(str, YArr))} -> S3\nLooping...\n{s_line}')
            exit()
        # S3 -> S6
        elif XArr[14] == '1':
            print(f'S3 -> {" ".join(map(str, YArr))} -> S6')
            state = 'S6'

    # --S4--
    if state == 'S4':
        # S4 -> S2
        if ((XArr[15] == '1' and XArr[11] == '0') or
                (XArr[15] == 1 and XArr[11] == '1' and XArr[13] == '0' and XArr[1] == '0' and XArr[10] == '0')):
            YArr[10] = 1
            YArr[11] = 1
            print(f'S4 -> {" ".join(map(str, YArr))} -> S2')
            state = 'S2'
            YArr[10] = 0
            YArr[11] = 0
            check_state(XArr, state, count)

        # S4 -> S4
        elif XArr[15] == '0':
            print(f'S4 -> {" ".join(map(str, YArr))} -> S4\nLooping...\n{s_line}')
            exit()
        # S4 -> S5
        elif XArr[15] == '1' and XArr[11] == '1' and XArr[13] == '1':
            YArr[17] = 1
            YArr[18] = 1
            YArr[20] = 1
            print(f'S4 -> {" ".join(map(str, YArr))} -> S5')
            state = 'S5'
            YArr[17] = 0
            YArr[18] = 0
            YArr[20] = 0

        # S4 -> S6
        elif XArr[15] == '1' and XArr[11] == '1' and XArr[13] == '0' and XArr[1] == '0' and XArr[10] == '1':
            YArr[23] = 1
            print(f'S4 -> {" ".join(map(str, YArr))} -> S6')
            state = 'S6'
            YArr[23] = 0

        # S4 -> S7
        elif XArr[15] == '1' and XArr[11] == '1' and XArr[13] == '0' and XArr[1] == '1':
            YArr[1] = 1
            YArr[15] = 1
            YArr[19] = 1
            print(f'S4 -> {" ".join(map(str, YArr))} -> S7')
            state = 'S7'
            YArr[1] = 0
            YArr[15] = 0
            YArr[19] = 0

    # --S5--
    if state == 'S5':
        # S5 -> S3
        if XArr[8] == '1' and XArr[7] == '1':
            YArr[5] = 1
            YArr[7] = 1
            YArr[9] = 1
            YArr[13] = 1
            print(f'S5 -> {" ".join(map(str, YArr))} -> S3')
            state = 'S3'
            YArr[5] = 0
            YArr[7] = 0
            YArr[9] = 0
            YArr[13] = 0
            check_state(XArr, state, count)

        # S5 -> S5
        elif XArr[8] == '0':
            print(f'S5 -> {" ".join(map(str, YArr))} -> S5\nLooping...\n{s_line}')
            exit()
        # S5 -> S6
        elif XArr[8] == '1' and XArr[7] == '0':
            YArr[12] = 1
            print(f'S5 -> {" ".join(map(str, YArr))} -> S6')
            state = 'S6'
            YArr[12] = 0

    # --S6--
    # S6 -> S8
    if state == 'S6':
        YArr[22] = 1
        print(f'S6 -> {" ".join(map(str, YArr))} -> S8')
        state = 'S8'
        YArr[22] = 0

    # --S7--
    if state == 'S7':
        # S7 -> S6
        if XArr[9] == '1':
            YArr[14] = 1
            print(f'S7 -> {" ".join(map(str, YArr))} -> S6')
            state = 'S6'
            YArr[14] = 0
            check_state(XArr, state, count)

        # S7 -> S7
        elif XArr[9] == '0':
            print(f'S7 -> {" ".join(map(str, YArr))} -> S7\nLooping...\n{s_line}')
            exit()
    # --S8--
    # S8 -> S9
    if state == 'S8':
        YArr[6] = 1
        YArr[7] = 1
        YArr[24] = 1
        print(f'S8 -> {" ".join(map(str, YArr))} -> S9')
        state = 'S9'
        YArr[6] = 0
        YArr[7] = 0
        YArr[24] = 0

    # --S9--
    if state == 'S9':
        # S9 -> S0
        if XArr[15] == '1':
            YArr[25] = 1
            print(f'S9 -> {" ".join(map(str, YArr))} -> S0\n{s_line}')
            YArr[25] = 0
            exit()
        # S9 -> S9
        elif XArr[15] == '0':
            print(f'S9 -> {" ".join(map(str, YArr))} -> S9\nLooping...\n{s_line}')
            exit()


while True:
    with open('input-course.txt', 'r') as file:
        line = file.readline().strip()

    if len(line) == 15:
        XArr = list(line)
    else:
        print("Ошибка: Длина строки не равна 15")

    print('_' * 31)
    print(f'|          X1 - X15           |'
          f'\n|{" ".join(map(str, XArr))}|')
    print('|' + '_' * 29 + '|')
    XArr.insert(0, '#')

    method = input('Введите m для матрицы или g для граф-схемы: ')

    if method == 'm':
        matrix()
    elif method == 'g':
        state = 'S0'
        print(f'{s_line}\nStart S -> Y1-Y25 -> End S')
        graph_scheme(XArr, state, 1)
    elif method == 'e':
        print('Выход из программы.')
        break
    else:
        print('Ошибка в выборе метода.')
