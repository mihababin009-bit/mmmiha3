a = int(input('Введите число'))
while type(a) !=int:
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
if a % 2 ==0:
    print('четное')
else:
    print('нечетное')