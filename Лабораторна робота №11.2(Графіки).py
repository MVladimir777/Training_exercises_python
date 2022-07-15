'''
2. Задано ТРИ трикутники за допомогою координат вершин (вводить
користувач). Необхідно:
a. Перевірити чи такі трикутники існують.
b. Створити функцію перетворення кутів у радіани.
c. Побудувати трикутники кожен на своїх координатних осях.
d. Записати у файл (и) дані про площі та периметри кожного
трикутника.
e. Вивести на екран інформацію про те, який з трикутників має більшу
площу (1, 2 чи 3).
'''
from math import pi
from math import sqrt
import matplotlib.pyplot as plt

def grad_rad(kyt):
    rad = kyt * pi / 180
    return rad

def perevirka(a, b, c):
    if (a <= 0) or (b <= 0) or (c <= 0):
        print("Не існує відємної або нульової сторони.")
        m = False
    elif (a + b <= c) or (a + c <= b) or (c + b <= a):
        print("З відрізків такої довжини утворити трикутник неможливо.")
        m = False
    else:
        print('Такий трикутник існує')
        m = True
    return m

print('2. Задано ТРИ трикутники за допомогою координат вершин.')

x = []
y = []
for i in range(3):
    print('Трикутник', i+1)
    xx = []
    yy = []
    for j in range(3):
        print('Координата вершини', j+1)
        xx.append(float(input('x = ')))
        yy.append(float(input('y = ')))
    x.append(xx)
    y.append(yy)
    x[i].append(x[i][0])
    y[i].append(y[i][0])

for i in range(3):
    print(x[i])
print()

for i in range(3):
    print(y[i])
print()

z = []
for i in range(3):
    zz = []
    for j in range(3):
        zz.append(sqrt((x[i][j] - x[i][j+1])**2 + (y[i][j] - y[i][j+1])**2))
    z.append(zz)
    print(zz)
print()

for i in range(3):
    A,B,C = tuple(z[i])
    if perevirka(A,B,C) == False:
        exit(0)
print()

with open('Інформація про трикутники.txt', 'w') as f:
    area = []
    for i in range(3):
        print('Трикутник', i+1, file=f)
        P = sum(z[i])
        print('Периметр - {}'.format(P), file=f)
        p = P / 2
        S = sqrt(p*(p - z[i][0]) * (p - z[i][1]) * (p - z[i][2]))
        print('Площа - {}\n'.format(S), file=f)
        area.append(S)
        print('Периметр - {}'.format(P))
        print('Площа - {}\n'.format(S))
f.close()
print('Файли створено')


max = 0
i1 = 0
for i,elem in enumerate(area):
    if elem > max:
        max = elem
        i1 = i + 1
print('Найбільша площа {} y {} трикутника'.format(max, i1))

fig, ax = plt.subplots(nrows=1, ncols=3)
#Побудова графіка
ax[0].triplot(x[0], y[0], 'ro-', linestyle='dotted', linewidth=2, markersize=4)
ax[1].triplot(x[1], y[1], 'bo-', linestyle='dashed', linewidth=2, markersize=4)
ax[2].triplot(x[2], y[2], 'go-', linestyle='dashdot', linewidth=2, markersize=4)
#Сітка графіка
for i in range(3):
    ax[i].grid(color='silver', linestyle='--', linewidth=1)
#Підпис
for i in range(3):
    ax[i].set_title('Трикутник {}'.format(i+1))
#підпис осей
for i in range(3):
    ax[i].set_xlabel('x', rotation = 0)
    ax[i].set_ylabel('y', rotation = 0)
#додати текст
abc = ['A','B','C']
for i in range(3):
    for j in range(3):
        ax[i].text(x[i][j], y[i][j], abc[j], rotation = 0, fontsize = 14)
#показати графік
plt.show()