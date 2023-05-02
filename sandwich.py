sandwith_orders = ['сырный', 'рыбный', 'сырный', 'двойной', 'сырный', 'летний', 'с маслом']
finished_sandwith = []

while 'сырный' in sandwith_orders:
    sandwith_orders.remove('сырный')
print(sandwith_orders)
while sandwith_orders:
    sandwith = sandwith_orders.pop()
    print(f'Заказали сэндвитч {sandwith}')
    finished_sandwith.append(sandwith)
print('\n')
for sandwith in finished_sandwith:
    print(f'Приготовили сэндвитч {sandwith}')