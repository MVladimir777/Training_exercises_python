print('''1. Користувач вводить Ім'я, електронну адресу та номер телефону.
Переконатися, що дані введено коректно:
а) ім'я повинно містити тільки символи
б) в адресі наявний символ @ і крапка після нього, а також наявні
   принаймні два символи після останньої крапки
в) телефон повинен містити тільки цифри''')

print('\nПривіт')
im = input("Введіть ваше ім'я - ")
m = True
while m == True:
    for elem in im:
        if (ord('А') > ord(elem)) or (ord(elem) > ord('ї')):
            m = False
    if m == False:
        im = input("Ваше ім'я повинно складається із українських символів - ")
        m = True
    else:
        m = False


email = input('Введіть електронну адресу - ')
m = False
while m == False:
    for i in range(len(email)):
        if email[i] == '@':
            i1 = i
        elif email[i] == '.':
            i2 = i
    m = bool((('@' in email) == False) or (('.' in email) == False)
             or (i1 > i2) or (i2 > (len(email)-3)) or (i1 == 0))
    if m == True:
        email = input('Введіть електронну адресу правильно - ')
        m = False
    else:
        m = True


tel = input('Введіть ваш номер телефону - ')
m = True
while m == True:
    for elem in tel:
        if (elem in ['0','1','2','3','4','5','6','7','8','9']) == False:
            m = False
    if m == False:
        tel = input('Ваш номер телефона повинен містити тільки цифри - ')
        m = True
    else:
        m = False


print("\nВаше ім'я -",im)
print("Електронна ареса -",email)
print("Номер телефону -",tel)