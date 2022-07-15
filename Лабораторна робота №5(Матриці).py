#Задача 1===============================================================
import random
print('''1. Дано цілі числа a1, a2, a3. Отримати цілочисельну матрицю |b(i,j)|
i,j=1,2,3, для якої b(i,j)=ai − 3aj.''')
v = int(input('Автоматичне заповнення (1)\ Ручне заповнення (2) - '))
n = 3
if v == 1:
    a = [random.randint(1, 10) for i in range(n)]
elif v == 2:
    a = [int(input('a%i = ' %(i+1))) for i in range(n)]
print('a -',a)

b = []
for i in range(len(a)):
    c = [a[i]-3*a[j] for j in range(len(a))]
    b.append(c)
    print(c)


#Задача 2===============================================================
import random
print('''\n2. Дано дійсну матрицю розміру nxm. Отримати нову матрицю шляхом
ділення усіх елементів даної матриці на її найбільший за модулем елемент.''')
v = int(input('Автоматичне заповнення (1)\ Ручне заповнення (2) - '))
n = int(input('Кількість рядків n = '))
m = int(input('Кількість стовпчиків m = '))
if v == 1:
    a = []
    for i in range(n):
        b = [random.randint(1, 10) for j in range(m)]
        a.append(b)
        print(b)
elif v == 2:
    a = []
    for i in range(n):
        b = [int(input('a%i%i = ' %(i+1,j+1))) for j in range(m)]
        a.append(b)
    for i in range(n):
        print(a[i])

max1 = max([max(a[i]) for i in range(n)])
print('Максимальне',max1)

b = a.copy()
b = [[b[i][j]/abs(max1) for j in range(m)] for i in range(n)]
for i in range(n):
    print(b[i])


#Задача 3===============================================================
import random
print('''\n3. Дано дійсну квадратну матрицю порядку n(n<=10). Замінити нулями
усі її елементи, розташовані на головній діагоналі.''')
v = int(input('Автоматичне заповнення (1)\ Ручне заповнення (2) - '))
n = int(input('Квадратна матриця порядку n(n<=10) = '))
while n > 10:
    n = int(input('Введіть n<=10 - '))

if v == 1:
    a = []
    for i in range(n):
        b = [random.randint(1, 10) for j in range(n)]
        a.append(b)
        print(b)
elif v == 2:
    a = []
    for i in range(n):
        b = [int(input('a%i%i = ' %(i+1,j+1))) for j in range(n)]
        a.append(b)
    for i in range(n):
        print(a[i])

print()
b = a.copy()
for i in range(n):
    for j in range(n):
        if i == j:
            b[i][j] = 0
    print(b[i])


#Задача 4===============================================================
import random
print('\n4. Дано дійсну матрицю розміру nxm.')
v = int(input('Автоматичне заповнення (1)\ Ручне заповнення (2) - '))
n = int(input('Кількість рядків n = '))
m = int(input('Кількість стовпчиків m = '))
if v == 1:
    a = []
    for i in range(n):
        b = [random.randint(1, 10) for j in range(m)]
        a.append(b)
        print(b)
elif v == 2:
    a = []
    for i in range(n):
        b = [int(input('a%i%i = ' %(i+1,j+1))) for j in range(m)]
        a.append(b)
    for i in range(n):
        print(a[i])
        
print('Створити списокn b1 , ..., bm , кожен елемент якого – це, відповідно:')        
b1 = [sum(a[i]) for i in range(n)]
print('а) сума елементів кожного рядку матриці -',b1)

b2 = []
for i in range(n):
    d = 1
    for j in range(m):
        d *= a[i][j]
    b2.append(d)
print('б) добуток елементів кожного рядку матриці -',b2)


#Задача 5===============================================================
import random
print('''\n5. Дано дійсну матрицю розміру nxm. У кожному рядку знайти елемент
з найменшим та найбільшим значеннями. Вказати індекси цих елементів.''')
v = int(input('Автоматичне заповнення (1)\ Ручне заповнення (2) - '))
n = int(input('Кількість рядків n = '))
m = int(input('Кількість стовпчиків m = '))
if v == 1:
    a = []
    for i in range(n):
        b = [random.randint(1, 10) for j in range(m)]
        a.append(b)
        print(b)
elif v == 2:
    a = []
    for i in range(n):
        b = [int(input('a%i%i = ' %(i+1,j+1))) for j in range(m)]
        a.append(b)
    for i in range(n):
        print(a[i])

for i in range(n):
    max = a[i][0]
    min = a[i][0]
    j1 = 0
    j2 = 0
    for j,elem in enumerate(a[i]):
        if elem > max:
            max = elem
            j1 = j
        if elem < min:
            min = elem
            j2 = j   
    print('Рядок',i+1)
    print('Максимум - %i, індекси - [%i,%i]'%(max,i,j1))
    print('Мінімум - %i, індекси - [%i,%i]'%(min,i,j2))


#Задача 6===============================================================
import random
print('''\n6. Дано дійсну матрицю розміру nxm. Знайти середнє арифметичне
значення елементів рядків.''')
v = int(input('Автоматичне заповнення (1)\ Ручне заповнення (2) - '))
n = int(input('Кількість рядків n = '))
m = int(input('Кількість стовпчиків m = '))
if v == 1:
    a = []
    for i in range(n):
        b = [random.randint(1, 10) for j in range(m)]
        a.append(b)
        print(b)
elif v == 2:
    a = []
    for i in range(n):
        b = [int(input('a%i%i = ' %(i+1,j+1))) for j in range(m)]
        a.append(b)
    for i in range(n):
        print(a[i])

for i in range(n):
    b = sum(a[i])/m
    print('Середє значення %i рядка - %f' %(i+1,b))
