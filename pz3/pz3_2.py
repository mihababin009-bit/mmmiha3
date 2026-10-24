try:
    amount = float(input('Введите сумму вклада (в рублях): '))
    if amount<0:
        print('неправильно отрицательно.')
    else:
        if amount < 50000:
            rate = 4
        elif 50000 <= amount < 100000:
            rate = 5
        elif 100000 <= amount < 150000:
            rate = 6
        elif 150000 <= amount < 200000:
            rate = 7
        else:
            rate = None
    if rate is not None:
        print(f'Процентаная ставка длясуммы{amount:.2f} р. составит {rate}%.')
    else:
        print('Для сумм выше 200 000р. процеентная ставка не определена условием.')
except ValueError:
    print('неправильно')
