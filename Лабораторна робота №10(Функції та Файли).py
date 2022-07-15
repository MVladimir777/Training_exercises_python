#Задача 1===============================================================
from random import randint

def maxmod(x, s):
    y = [max(x[i], key=abs) for i in range(s)]
    z = abs(max(y, key=abs))
    print('Найбільший за модулем елемент -', z)
    return z

print('''1. Дано дійсну матрицю розміру m на n. Отримати нову матрицю шляхом
 ділення усіх елементів даної матриці на її найбільший за модулем елемент.
 Пошук найбільшого за модулем елементу винести у окрему функцію. Нову
 отриману матрицю записати у файл.''')

n = int(input('Кількість рядків n = '))
m = int(input('Кількість стовпчиків m = '))
a = [[randint(-10, 10) for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        print("%4d" % a[i][j], end='')
    print()

b = maxmod(a, n)
c = [[a[i][j]/b for j in range(m)] for i in range(n)]

with open('Матриця.txt', 'w') as f:
    for i in range(n):
        print(c[i], file = f)
    f.close()
    print('Файл створено')


#Задача 2===============================================================
from random import randint

def zamina(x, y):
    for i in range(y):
        x[i][i] = 0
        for j in range(y):
            print("%4d" % x[i][j], end='')
        print()

print('''\n2. Дано квадратну матрицю дійсних чисел порядку n(n<=10). Замінити
 нулями усі її елементи, розташовані на головній діагоналі (у функції).
 Записати у файл елементи головної діагоналі ДО заміни її нулями.''')

n = int(input('Розмірність матриці n = '))
while n > 10:
    n = int(input('Введіть нове значення згідно умови n = '))

a = [[randint(-10, 10) for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        print("%4d" % a[i][j], end='')
    print()

with open('Головна діагональ.txt', 'w') as f:
    b = [a[i][i] for i in range(n)]
    f.write(str(b))
    f.close()
    print('Файл створено')

zamina(a, n)


#Задача 3===============================================================
from random import randint

def seredne(x, y, z):
    d = {}
    for i in range(y):
        s = 'Рядок {}'.format(i+1)
        d[s] = sum(x[i])/z
    return d

print('''\n3. Дано дійсну матрицю розміру m на n. Знайти середнє арифметичне
 значення елементів кожного рядка (у функції). Записати результат у файл.''')

n = int(input('Кількість рядків n = '))
m = int(input('Кількість стовпчиків m = '))
a = [[randint(-10, 10) for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        print("%4d" % a[i][j], end='')
    print()

with open('Середні значення.txt', 'w') as f:
    b = seredne(a, n, m)
    for k,v in b.items():
        print(k, ':', v, file=f)
        print(k, ':', v)
    f.close()
    print('Файл створено')


#Задача 4===============================================================
from random import randint

def maxsumalne(x, y, z):
    d = {}
    for i in range(y):
        maxs = 0
        s = 'Рядок {}'.format(i + 1)
        for j in range(z):
            if x[i][j] > maxs:
                maxs = x[i][j]
        d[s] = maxs
    return d

def minimalne(x, y, z):
    d = {}
    for i in range(y):
        mini = 0
        s = 'Рядок {}'.format(i + 1)
        for j in range(z):
            if x[i][j] < mini:
                mini = x[i][j]
        d[s] = mini
    return d

print('''\n4. Дано дійсну матрицю розміру m на n. Знайти найбільше та найменше
 значення елементів кожного рядка (у функціях). Записати результат у файл.''')

n = int(input('Кількість рядків n = '))
m = int(input('Кількість стовпчиків m = '))
a = [[randint(-10, 10) for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        print("%4d" % a[i][j], end='')
    print()

print('Максимальне', maxsumalne(a, n, m))
print('Mінімальне', minimalne(a, n, m))

with open('Максимальне і мінімальне.txt', 'w') as f:
    print('Максимальне', maxsumalne(a, n, m), file = f)
    print('Mінімальне', minimalne(a, n, m), file = f)
    f.close()
    print('Файл створено')


#Задача 5===============================================================
from random import randint

def minmax(x, y):
    min = x[0]
    max = x[0]
    for i in range(y):
        if x[i] < min:
            min = x[i]
        if x[i] > max:
            max = x[i]
    return min, max

print('''\n5. Обчислити суму елементів числового списку, які розташовані між
 позиціями максимального та мінімального елементів. Вважати, що всі
 елементи списку різні. Пошук максимуму та мінімуму винести у функцію.
 Частину списку між макимальним та мінімальним елементом записати у файл.''')

n = int(input('Розмір списку n = '))
a = [randint(1, 10) for i in range(n)]
print(a)

s = a.copy()
b, c = minmax(a, n)
if s.index(b) < s.index(c):
    s[:s.index(b)+1] = []
    s[s.index(c):] = []
else:
    s[s.index(b):] = []
    s[:s.index(c)+1] = []
print('Сума елементів',s,'=',sum(s))

with open('Список.txt', 'w') as f:
    f.write(str(s))
    f.close()
    print('Файл створено')