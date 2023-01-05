from random import randint

N = int(input())
number = input()
step = int(input())
mas = list(number.split(" "))
k = 0
for i in range(step):
    for j in range(N - i):
        if mas[j] > mas[j + 1]:
            mas[j], mas[j + 1] = mas[j + 1], mas[j]
            k+=1
            if k == step:
                break


print(*mas)