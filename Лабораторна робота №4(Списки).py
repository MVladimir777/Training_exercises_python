#Задача 1===============================================================
import random
print('1. Вивести на екран список, який складається з факторіалів чисел від 1 \nдо n, де n – введене з клавіатури число.')
n = int(input('Число n = '))
a = []
for i in range(1, n+1):
    b = 1
    for j in range(1, i+1):
        b *= j
    a.append(b)
print(a)


#Задача 2===============================================================
import random
print('\n2. Дано список натуральних чисел. Знайти кількість:')
v = int(input('Автоматичне заповнення (1)\ Ручне заповнення (2) - '))
n = int(input('Розмір списку n = '))
if v == 1:
    a = [random.randint(1, 100) for i in range(n)]
elif v == 2:
    a = [int(input('a%i = ' %i)) for i in range(n)]

kilpar = 0
kild = 0
kil0 = 0
kilpr = 0
for elem in a:
    if elem % 2 == 0:
        kilpar += 1        
    if (elem % 3 == 0) or (elem % 5 == 0):
        kild += 1        
    if elem == 0:
        kil0 += 1
    par = 0
    i = 2
    while i <= elem-1:
        if elem % i == 0:
            par = 1
        i += 1
    if par == 0:
        kilpr += 1

print(a)
print('a) парних компонентів\n', kilpar)
print('b) компонент, що діляться на 3 або 5\n', kild)
print('c) нульових компонент\n', kil0)
print('d) компонентів, що є простими числами\n', kilpr)


#Задача 3===============================================================
import random
import math
print('\n3. Дано список натуральних чисел.')
v = int(input('Автоматичне заповнення (1)\ Ручне заповнення (2) - '))
n = int(input('Розмір списку n = '))
if v == 1:
    a = [random.randint(1, 100) for i in range(n)]
elif v == 2:
    a = [int(input('a%i = ' %i)) for i in range(n)]
print(a)

print('Використовуючи оператор створення списку, побудувати список, що містить:')
b = [elem for elem in a if elem % 2 == 0]
c = [elem for elem in a if math.sqrt(elem) % 1 == 0]
d = [elem**2 for elem in a if elem % 2 != 0]

print('a) всі парні елементи заданого списку;\n', b)
print('b) всі елементи заданого списку, що є повними квадратами\n', c)
print('c) квадрати непарних компонент заданого списку\n', d)


#Задача 4===============================================================
import random
import math
print('\n4. Дано список чисел. Знайти кількість елементів списку, більших\менших\n за задане число k.')
v = int(input('Автоматичне заповнення (1)\ Ручне заповнення (2) - '))
n = int(input('Розмір списку n = '))
k = int(input('Число k = '))
if v == 1:
    a = [random.randint(-100, 100) for i in range(n)]
elif v == 2:
    a = [int(input('a%i = ' %i)) for i in range(n)]
print(a)

kilb = 0
kill = 0
for elem in a:
    if elem > k:
        kilb += 1
    elif elem < k:
        kill += 1
print('a) Кількість більших -', kilb)
print('b) Кількість менших -', kill)


#Задача 5===============================================================
import random
print('\n5. Обчислити суму елементів числового списку, які розташовані між позиціями \nмаксимального та мінімального елементів. Вважати, що всі елементи списку різні.')
v = int(input('Автоматичне заповнення (1)\ Ручне заповнення (2) - '))
n = int(input('Розмір списку n = '))
if v == 1:
    a = [random.randint(1, 100) for i in range(n)]
elif v == 2:
    a = [int(input('a%i = ' %i)) for i in range(n)]
print(a)

s = a.copy()
if s.index(min(s)) < s.index(max(s)):
    s[:s.index(min(s))+1] = []
    s[s.index(max(s)):] = []
else:
    s[s.index(min(s)):] = []
    s[:s.index(max(s))+1] = []
print('Сума елементів',s,'=',sum(s))


#Задача 6===============================================================
import random
print('\n6. Задано натуральне число n і список натуральних чисел А, a1, . . . , an.')
v = int(input('Автоматичне заповнення (1)\ Ручне заповнення (2) - '))
n = int(input('Розмір списку n = '))
A = int(input("Число А = "))
if v == 1:
    a = [random.randint(-100, 100) for i in range(n)]
elif v == 2:
    a = [int(input('a%i = ' %(i+1))) for i in range(n)]
print(a)

print("a) Знайти номер члена списку a1, . . . , an, який дорівнює А.\n Якщо такого члена списку немає, то результатом має бути число 0")
if (A in a) == False:
    print("Члена списку рівного А немає. Результат 0")
else:
    for i in range(n):
        if A == a[i]:
            print("Номер елемента %d" %(i+1))

print("b) Якщо в списку a1, . . . , an є хоча б один член, що дорівнює А, то\n отримати суму всіх членів, які йдуть ЗА таким членом списку. ")
print(" У протилежному випадку відповіддю має бути відповідне текстове повідомлення.")
s = []
if (A in a) == False:
    print("Члена списку рівного А немає.")
else:
    s = a.copy()
    ind = s.index(A)
    s[:ind+1] = []            
print("Сума",sum(s))

print("c) Отримати суму додатних, кількість від’ємних і число нульових членів списку\n a1, . . . , an.")
sum1 = 0
nom1 = 0
nom2 = 0
for i in range(n):
    if a[i] > 0:
        sum1 += a[i]
    elif a[i] == 0:
        nom1 += 1
    else:
        nom2 += 1
print("Сума додатніх:",sum1)
print("Кількість від’ємних:",nom2)
print("Число нульових членів:",nom1)
print(sum([elem for elem in a if elem > 0])) #Другий варіант для знаходження відповіді
print(len([elem for elem in a if elem < 0]))
print(len([elem for elem in a if elem == 0]))


#Задача 7===============================================================
import random
print('\n7. Задано натуральні числа n і p та список a1, . . . , an. Скласти\n програму обчислення добутку членів списку, кратних p.')
v = int(input('Автоматичне заповнення (1)\ Ручне заповнення (2) - '))
n = int(input('Розмір списку n = '))
p = int(input("Число p = "))
if v == 1:
    a = [random.randint(1, 100) for i in range(n)]
elif v == 2:
    a = [int(input('a%i = ' %i)) for i in range(n)]
print(a)

m = 0
dob = 1
for i in range(n):
    if a[i] % p == 0:
        dob *= a[i]
        m = 1
if m == 1:
    print("Добуток чисел:",dob)
else:    
    print("Немає кратних",p)


#Задача 8===============================================================
import random
print('\n8. Задані натуральне число n, список a1, a2, . . . , an.\n Написати програми для знаходження:')
v = int(input('Автоматичне заповнення (1)\ Ручне заповнення (2) - '))
n = int(input('Розмір списку n = '))
if v == 1:
    a = [random.randint(-100, 100) for i in range(n)]
elif v == 2:
    a = [int(input('a%i = ' %(i+1))) for i in range(n)]
print(a)
print("a) min(a1,a2,...,an)")
print("min =", min(a))
print("b) max(|a1|,...,|an|)")
print("max =", abs(max(a,key=abs)))
print("c) max(a2,a4,...)")
print("max =",max(a[1::2]))
print("d) min(a1,a3,...)")
print("min =",min(a[::2]))


#Задача 9===============================================================
import random
print('\n9. Задано список символів. Знайти його довжину. Всі літери j у списку')
print('замінити на літери k. Якщо такої літери немає у списку, то створити її на')
print('початку та в кінці списку, а потім замінити на f. Всі проміжні списки')
print('виводити на екран для перевірки правильності замін.')
v = int(input('Автоматичне заповнення (1)\ Ручне заповнення (2) - '))
if v == 1:
    a = list('qwejajajazxc')
elif v == 2:
    a = list(input('Уведіть набір символів - '))
print(a)

print('Довжина списку -',len(a))

if ('j' in a) == True:
    for i,elem in enumerate(a):
        if elem == 'j':
            a[i] = 'k'
    print(a)
else:
    a.insert(0,'j')
    a.append('j')
    print(a)
    for i,elem in enumerate(a):
        if elem == 'j':
            a[i] = 'f'
    print(a)


#Задача 10==============================================================
import random
print('\n10. Знайти спільну компоненту двох списків.')
v = int(input('Автоматичне заповнення (1)\ Ручне заповнення (2) - '))
n = int(input('Розмір списку n = '))
if v == 1:
    a = [random.randint(1, 10) for i in range(n)]
    b = [random.randint(1, 10) for i in range(n)]
elif v == 2:
    a = [int(input('a%i = ' %i)) for i in range(n)]
    b = [int(input('a%i = ' %i)) for i in range(n)]
print(a, '\n', b)
print([elem for elem in a if (elem in b) == True])
print(list(set(a) & set(b))) #Другий варіант для знаходження спільних компонентів (робить унікальний список)


#Задача 11==============================================================
import random
print('\n11. Перевірити чи впорядкований числовий список за зростанням.')
v = int(input('Автоматичне заповнення (1)\ Ручне заповнення (2) - '))
n = int(input('Розмір списку n = '))
if v == 1:
    p = random.randint(0, 1)
    if p == 0:
        a = [random.randint(-100, 100) for i in range(n)]
    else:
        a = [random.randint(-100, 100)]
        i = 1
        while i != n:
            x = random.randint(-100, 100)
            if a[i-1] <= x:
                a.append(x)
                i += 1
elif v == 2:
    a = [int(input('a%i = ' %i)) for i in range(n)]

m = 0
m1 = 0
for i in range(len(a)-1):
    if a[i] <= a[i+1]:
        m = 1
    else:
        m1 = 1
        
if m1 == 1:    
    print("Відповідь: Непорядковано за зростанням",a)
elif m == 1:
    print("Відповідь: Впорядковано за зростанням",a)


#Задача 12==============================================================
print('\n12. Маємо список [23, 32, 56, 65, 98, 89, 12, 21, 45, 54, 87, 78].\nНе дізнаючись його довжину додайте новий елемент 100 у ПЕРЕДОСТАННЮ позицію.')
a = [23, 32, 56, 65, 98, 89, 12, 21, 45, 54, 87, 78]
a.insert(-1, 100)
print(a)


#Додаткове завдання=====================================================
print('\nВивести ряди арифметичної i геометричної прогресій')
n = int(input('Кількість елементів прогресії n = '))
a = [int(input('Перший елемент прогресії а1 = '))]
d = int(input('Різниця арифметичної прогресії d = '))
q = int(input('Знаменник геометричної прогресії q = '))
g = a.copy()
for i in range(n):
    a.append(a[-1] + d)
    g.append(g[-1] * q)
print('Арифметична прогреся -', a)
print('Геометрична прогреся -', g)
