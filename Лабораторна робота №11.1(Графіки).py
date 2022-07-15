'''1. Кидають ДВА тіла під певними кутами до горизонту. Кути кидання відомі
(задає користувач), початкові швидкості відомі (задає користувач).
Необхідно:
a. Створити функцію перетворення кутів у радіани.
b. Побудувати траєкторії руху обох тіл на одній координатній осі.
c. Записати у файл (и) дані про координати тіл у кожен момент часу,
тобто (t, x, y).
d. Знайти дальність польоту та максимальну висоту підняття тіл
ДВОМА способами:
1 – пошук максимального у та х,
2 – за допомогою фізичних рівнянь.
Вивести отримані двома способами значення, для наочного
порівняння'''

from math import pi
from math import sin
from math import cos
import matplotlib.pyplot as plt

def grad_rad(kyt):
    rad = kyt * pi / 180
    return rad

def ox_oy(v, a):
    g = 9.8
    time = 2 * v * sin(grad_rad(a)) / g
    x = []
    t = 0
    while t <= time:
        x.append(v * cos(grad_rad(a)) * t)
        t += 0.1
    x.append(v ** 2 * sin(grad_rad(2 * a)) / g)

    y = []
    t = 0
    while t <= time:
        y.append(v * sin(grad_rad(a)) * t - g * t ** 2 / 2)
        t += 0.1
    y.append(0)

    return x, y

print('Кидають ДВА тіла під певними кутами до горизонту.')

alf01 = float(input('Введіть кут кидання першого тіла у градусах - '))
v01 = float(input('Введіть початкову швидкість першого тіла - '))
alf02 = float(input('Введіть кут кидання другого тіла у градусах - '))
v02 = float(input('Введіть початкову швидкість другого тіла - '))

x1, y1 = ox_oy(v01, alf01)
x2, y2 = ox_oy(v02, alf02)

f = open('Координати тіла 1.txt', 'w')
for i in range(len(x1)):
    print('{} - {}    {}'.format(i, x1[i], y1[i]), file = f)
f.close()

f = open('Координати тіла 2.txt', 'w')
for i in range(len(x2)):
    print('{} - {}    {}'.format(i, x2[i], y2[i]), file = f)
f.close()
print('Файли створено')

print('Тіло перше')
print(v01 ** 2 * sin(grad_rad(2 * alf01)) / 9.8, '-', max(x1[:-1]))
print(v01 ** 2 * sin(grad_rad(alf01)) ** 2 / (2 * 9.8), '-', max(y1))
print('Тіло друге')
print(v02 ** 2 * sin(grad_rad(2 * alf02)) / 9.8, '-', max(x2[:-1]))
print(v02 ** 2 * sin(grad_rad(alf02)) ** 2 / (2 * 9.8), '-', max(y2))

fig, ax = plt.subplots(1, 1)
#Побудова графіка
ax.plot(x1, y1, color='green', marker='o', linestyle='solid', linewidth=2, markersize=3)
ax.plot(x2, y2, color='blue', marker='o', linestyle='solid', linewidth=2, markersize=3)
#Сітка графіка
ax.grid(color='silver', linestyle='--', linewidth=1)
#межі осей
if max(x1) > max(x2):
    ax.set_xlim([min(x2) - 1, max(x1) + 1])
else:
    ax.set_xlim([min(x1) - 1, max(x2) + 1])
if max(y1) > max(y2):
    ax.set_ylim([min(y1) - 1, max(y1) + 1])
else:
    ax.set_ylim([min(y2) - 1, max(y2) + 1])
#Підпис
ax.set_title('Графік траєкторій')
#підпис осей
ax.set_xlabel('x', rotation = 0)
ax.set_ylabel('y', rotation = 0)
#додати текст
ax.text(x1[5], y1[5], 'v1',
        rotation = 0, #Кут нахилу напису
        fontsize = 14)  #Розмір шрифта
ax.text(x2[5], y2[5], 'v2', rotation = 0, fontsize = 14)
#показати графік
plt.show()