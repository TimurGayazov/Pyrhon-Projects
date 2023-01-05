n = int(input())
number = input()
step = int(input())
mas = list(number.split(" "))
print(mas)

for j in range(0,n):
    f = 0
    for i in range(0,n-j):
        if mas[i] > mas[i+1]:
            t = mas[i]
            mas[i] = mas[i+1]
            mas[i + 1] = t
        f = 1
    if f == 0:
        break

print(mas)