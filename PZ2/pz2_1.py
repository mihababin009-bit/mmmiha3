A=input('Введите число 1 -')
Y=input('Введите число 2 -')
X=input('Введите число 3 -')
B=input('Введите число 4 -')
while type(A) != int and type(B) != int and type(X) != int and type(Y) != int:
    try:
        A = int(A)
        X = int(X)
        Y = int(Y)
        B = int(B)
    except ValueError:
        print('Вы ввели не число!')
        A = input('Введите число 1 -')
        Y = input('Введите число 2 -')
        X = input('Введите число 3 -')
        B = input('Введите число 4 -')
cena1 = A/X
cena2 = B/Y
otnoshenie = cena1/cena2
print('1 кг шоколадных конфет стоит', cena1,'руб.')
print('1 кг ирисок стоит', cena2,'руб.')
print('Шоколадные конфеты дороже в',otnoshenie, 'раза.')