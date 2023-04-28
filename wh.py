ticket = True
while ticket:
    age = int(input('Введите возраст: '))
    if age == 999:
        ticket = False
    else:
        if age <= 3:
            rate = 'детский'
            price = 0
            print(f'Ваш тариф "{rate.title()}" цена: {price} рублей')
        elif 3 < age < 12:
            rate = 'подросток'
            price = 200
            print(f'Ваш тариф "{rate.title()}" цена: {price} рублей')
        else:
            rate = 'взрослый'
            price = 500
            print(f'Ваш тариф "{rate.title()}" цена: {price} рублей')