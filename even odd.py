promt = 'Сейчас будет проведенна проверка на четность числа'
promt += '\nВведите число: '
number = int(input(promt))
if number % 2 == 0:
    print(f'Число {number} четное')
else:
    print(f'Число {number} нечетное')