#Задача 1===============================================================
from math import pi

print('''1. Створити функцію перетворення кутів у радіани. Користувач одночаснно
 вводить 5 кутів.''')
kyt = lambda x: x * pi / 180
dic = {}
for i in range(1,6):
    k = int(input('Введіть кут {} - '.format(i)))
    dic[k] = kyt(k)

print()
for key in dic:
    print(key, ': ', dic[key])


#Задача 2===============================================================
from math import sin

def table(x1, x2, dx):
    dic = {}
    while x1 <= x2:
        dic[x1] = sin(x1)
        x1 += dx
    return dic

print('''\n2. Для функції sin(x) потрібно побудувати таблицю її значень.
 Користувач задає діапазон по х та крок dx.''')
a = float(input('Введіть ліву межу у радіанах - '))
b = float(input('Введіть праву межу у радіанах - '))
de = float(input('Введіть крок dx = '))

print()
f = table(a, b, de)
for key in f:
    print(key, ': ', f[key])


#Задача 3===============================================================
def vuraz1(a, b):
    s = '1'
    for i in range(2, b + 1, 2):
        s += '+' + str(x ** i)
    return s

def vuraz2(a, b):
    v = 0
    for i in range(0,b + 1,2):
        v += a ** i
    return v

print('\n3. Обчислити значення виразу 1 + x^2 + x^4 + .. + x^n.')
x = int(input('Введіть x = '))
n = int(input('Введіть n = '))
print('Відповідь: {}={}'.format(vuraz1(x,n),vuraz2(x,n)))


#Задача 4===============================================================
def fib(n):
    s = [1, 1]
    for i in range(2,n):
        s.append(s[-1]+s[-2])
    yield s

print('''\n4. Створити генератор-функцію побудови чисел Фібоначчі. Використати її
 для виведення перших N чисел Фібоначчі.''')
N = int(input('Введіть число N = '))
f = fib(N)
print(next(f))

#Другий варіант
def fibonacci(n):
    fib_list = []
    fib1, fib2 = 0, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        fib_list.append(fib1)
    yield fib_list

n=int(input('введіть n='))
for fib in fibonacci(n):
    print(fib)


#Задача 5===============================================================
def shchaslyve(a):
    s = list(a)
    if len(s) != 6:
        return print('Число нещасливе')
    else:
        if sum(s[0: 3]) == sum(s[3: 7]):
            return print('Число щасливе')
        else:
            return print('Число нещасливе')

print('''\n5. Щасливим називають таке шестизначне число, у якого сума перших трьох
 дорівнює сумі останніх трьох. Визначити чи будуть задані n чисел щасливими.''')
n = int(input('Введіть число - '))
k = 1
b = []
while n//k != 0:
    k *= 10
    b.append(int(n%k//(k/10)))
shchaslyve(b)


#Задача 6===============================================================
from math import sqrt

def kvadrat(a):
    if sqrt(a)%1 == 0:
        return True
    else:
        return False

print('''\n6. Дано натуральне число n. Для чисел від 1 до n визначити всі такі,
 які можна назвати повними квадратами числа. Описати функцію, яка перевіряє, 
 чи є число повним квадратом.''')
n = int(input('Введіть n = '))
s = []
for i in range(1, n+1):
    if kvadrat(i) == True:
        s.append(i)
print('Повні квадрати:',s)


#Задача 7===============================================================
import  random

#Перший варіант визначення символа, який трапляється частіше.
def spusok(s):
    dic = {}
    for elem in s:
        if elem not in dic:
            dic[elem] = s.count(elem)
    return dic

#Другий варіант визначення символа, який трапляється частіше.
def spusok1(s):
    chast = 0
    for elem in s:
        if s.count(elem) > chast:
            chast = s.count(elem)
            k = elem
    return k, chast

print('''7. Задано список символів, який може включати і цифри. Знайти, який 
символ трапляється частіше.''')
n = int(input('Введіть довжину списку n = '))
s1 = []
for i in range(n):
    s1.append(chr(random.randint(70, 75)))
print(s1)

d = spusok(s1)
print(d)

chasto = 0
for j, l in d.items():
    if l > chasto:
        chasto = l
        sumvol = j
print('Символ "{}" зустрічається {}'.format(sumvol, chasto))

print('Cимвол "{}" трапляється {}'.format(spusok1(s1)[0], spusok1(s1)[1]))