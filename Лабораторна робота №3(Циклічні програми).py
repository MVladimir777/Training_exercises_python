#Задача 1===============================================================
print("1. Вивести на екран такий рядок:")
s = "1"
N = int(input("N = "))
for i in range(2,N+1) :
    s += "*%u"%i
print("n!=",s)


#Задача 2===============================================================
print("\n2. Вивести на екран таблицю множення на 5:")
d = 0
for i in range(1,10):
    d += 5
    print("%u x 5 = %u"%(i,d))


#Задача 3===============================================================
print("\n3. Написати програму для обчислення добутку двох натуральних чисел, \nвикористовуючи лише операцію додавання.")
a = int(input("Число 1 = "))
b = int(input("Число 2 = "))
dob = 0
for i in range(1,a+1):
    dob += b
print("Відповідь:",dob)


#Задача 4===============================================================
print("\n4. Написати програму для обчислення факторіала натурального числа n!")
N = int(input("N = "))
w = 1
s = "1"
for i in range(2,N+1):
    w *= i
    s += "*%u"%i
print("n! = %s = %u" %(s,w))


#Задача 5===============================================================
print("\n5. Написати програми для обчислення факторіалів:")
n = int(input("Введіть число n = "))
a = 1
for i in range(1,2*n+1):
    a *= i
print("a) y = (2n)! =",a)

b = 1
for i in range(1,2*n+2):
    b *= i
print("b) y = (2n + 1)! =",b)

c = 1
d = 1
for i in range(1,n+2):
    c *= i
for i in range(1,n+1):    
    d *= i
print("c) y = n! (n + 1)! =",d*c)


#Задача 6===============================================================
import random
print("\n6. Задано натуральне число n і цілі числа a, a1, . . . , an.")
n = int(input("Введіть число n = "))
a = int(input("Число a = "))
print("a) Знайти номер члена послідовності a1, . . . , an, який дорівнює a. \nЯкщо такого члена послідовності немає, то результатом має бути число 0;")
m = 0
s = ""
for i in range(n):
    r = random.randint(1,10)
    s += " %u"%r
    if r == a:
        print("Номер елемента %d" %(i+1))
        m = 1
if m == 0:
    print("Номер елемента 0")    
print("Задані цілі числа:",s)

print("b) Якщо в послідовності a1, . . . , an є хоча б один член, що дорівнює \na, то отримати суму всіх членів, які йдуть за таким членом послідовності.")
print("У протилежному випадку відповіддю має бути відповідне текстове повідомлення.")
m = 0
s = ""
b = 0
sum =0
for i in range(n):
    r = random.randint(1,10)
    s += " %u"%r
    if r == a:
        print("Номер елемента %d" %(i+1))
        m = 1
        b = r
    if m == 1:
        sum += r     
if m == 0:        
    print("Немає такого числа")
sum = sum-b        
print("Сума",sum)    
print("Задані цілі числа:",s)

print("c) Отримати суму додатних, кількість від’ємних і число нульових членів \nпослідовності a1, . . . , an.")
s = ""
sum = 0
nom1 = 0
nom2 = 0
for i in range(n):
    r = random.randint(-10,10)
    s += " %u"%r
    if r > 0:
        sum += r
    elif r == 0:
        nom1 += 1
    else:
        nom2 += 1
print("Сума додатніх:",sum)        
print("Кількість від’ємних:",nom2)
print("Число нульових членів:",nom1)
print("Задані цілі числа:",s)


#Задача 7===============================================================
import random
print("\n7. Задано натуральні числа n і p та цілі числа a1, . . . , an. Скласти\n програму обчислення добутку членів послідовності, кратних p.")
n = int(input("Введіть число n = "))
p = int(input("Число p = "))
m = 0
s = ""
dob = 1
for i in range(n):
    r = random.randint(1,10)
    s += " %u"%r
    if r%p == 0:
        dob *= r 
        m = 1
if m == 1:
    print("Добуток чисел:",dob)
else:    
    print("Немає кратних",p)    
print("Задані цілі числа:",s)


#Задача 8===============================================================
import random
print("\n8. Задані натуральне число n, дійсні числа a1, a2, . . . , an.\n Написати програми для знаходження:")
n = int(input("Число n = "))    
print("a) min(a1,a2,a3,...,an)")
a = []
for i in range(1,n+1):
    a.append(random.randint(-10,10))
print("min",a,"=",min(a))

print("b) max(|a1|,...,|an|)")
print("max",a,"=",abs(max(a,key=abs)))

print("c) max(a2,a4,...)")
s = ""
a = []
for i in range(1,n+1):
    r = random.randint(-10,10)
    s += " %u"%r
    if i%2 == 0:
        a.append(r)        
print("max",a,"=",max(a))
print("Задані цілі числа:",s)

print("d) min(a1,a3,...)")
s = ""
a = []
for i in range(1,n+1):
    r = random.randint(-10,10)
    s += " %u"%r
    if i%2 != 0:
        a.append(r)      
print("min",a,"=",min(a))
print("Задані цілі числа:",s)

print("e) min(a2,a4,...)+max(a1,a3,...)")
s = ""
a = []
a1 = []
for i in range(1,n+1):
    r = random.randint(-10,10)
    s += " %u"%r
    if i%2 == 0:
        a.append(r)
    else:
        a1.append(r)
print(a,"\n",a1)
print(min(a),max(a1))
print("min(a2,a4,...)+max(a1,a3,...) =",min(a)+max(a1))
print("Задані цілі числа:",s)

print("f) max(a1,a2,a4,a8...)")
s = ""
p = 1
a = []
for i in range(1,n+1):
    r = random.randint(-10,10)
    s += " %u"%r
    if  i ==  p:
        a.append(r)
        p *= 2
print(a)       
print("max(a1,a2,a4,a8...) =",max(a))
print("Задані цілі числа:",s)

print("g) max(-a1,a2,-a3...,(-1)^n*an)")
s = ""
a = []
for i in range(1,n+1):
    r = random.randint(1,10)
    s += " %u"%(((-1)**i)*r)
    a.append(((-1)**i)*r)
print(a)
print("max(-a1,a2,-a3...,(-1)^n*an) =",max(a))
print("Задані цілі числа:",s)

print("h) max(a1,2*a2,...,n*an)")
s = ""
a = []
for i in range(1,n+1):
    r = random.randint(1,10)
    s += " %u"%(i*r)
    a.append(i*r)
print(a)
print("max(a1,2*a2,...,n*an =",max(a))
print("Задані цілі числа:",s)

print("i) (min(a1,...,an))^2-min(a1^2,...,an^2)")
s = ""
a = []
a1 = []
for i in range(1,n+1):
    r = random.randint(-10,10)
    s += " %u"%r
    a.append(r)
    a1.append(r**2)
print(a,"\n",a1)
print("(min(a1,...,an))^2-min(a1^2,...,an^2) =",min(a)**2-min(a1))
print("Задані цілі числа:",s)

print("j) max(a1+a2,...,a(n-1)+an)")
s = ""
a = []
a1 = []
for i in range(1,n+1):
    r = random.randint(-10,10)
    s += " %u"%r
    a.append(r)
if n%2 != 0:
    a.append(0)
for i in range(0,n,2):
    a1.append(a[i]+a[i+1])
print("Задані цілі числа:",s)
print("[a1+a2,...,a(n-1)+an] =",a1)
print("max(a1+a2,...,a(n-1)+an) =",max(a1))


#Задача 9===============================================================
import random
import math
print("\n9. Задані натуральне число n, натуральні числа a1, a2, . . . , an. \nНаписати програми для знаходження:")
n = int(input("Число n = "))
s = ""
k = 0
m = 0
for i in range(n):
    r = random.randint(1,10)
    s += " %u"%r
    if r%2 == 0:
        k += 1
        m = 1
if m == 0:
    print("a) кількості парних серед a1, a2, . . . , an НЕМАЄ")
else:    
    print("a) кількості парних серед a1, a2, . . . , an є",k)
print("Задані цілі числа:",s)

s = ""
k = 0
m = 0
for i in range(n):
    r = random.randint(1,10)
    s += " %u"%r
    if math.sqrt(r)%1 == 0:
        k += 1
        m = 1
if m == 0:
    print("b) кількості повних квадратів серед a1, a2, . . . , an НЕМАЄ")
else:    
    print("b) кількості повних квадратів серед a1, a2, . . . , an є",k)
print("Задані цілі числа:",s)

s = ""
k = 0
m = 0
for i in range(n):
    r = random.randint(1,10)
    s += " %u"%r
    if (r%2 != 0) and (math.sqrt(r)%1 == 0):
        k += 1
        m = 1
if m == 0:
    print("c) кількості квадратів непарних чисел серед a1, a2, . . . , an НЕМАЄ")
else:    
    print("c) кількості квадратів непарних чисел серед a1, a2, . . . , an є",k)
print("Задані цілі числа:",s)


#Задача 10==============================================================
import random
print("\n10. Дана непорожня послідовність різних натуральних чисел, за якою\n йде 0. Визначити порядковий номер найменшого з них.")
n = int(input("Кількість чисел n = "))
s = ""
min = 11
for i in range(n):
    r = random.randint(-10,10)
    s += " %u"%r
    if min > r:
        min = r
        a = i+1
print("Номер найменшого елемента %u" %a)
print("Задані цілі числа:",s)


#Задача 11==============================================================
print("\n11. Створити програму, яка з’ясовує, чи входить задана цифра до \nзапису заданого натурального числа.")
a = int(input("Задане число a = "))
b = int(input("Цифра b = "))
i = 1
m = 0
while a//i != 0:
    c = (a//i)%10
    if c == b:
        print("Цифра %u входить в число %u" %(b,a))
        m = 1
    i *= 10
if m == 0:
    print("Цифра %u НЕ входить в число %u" %(b,a))
