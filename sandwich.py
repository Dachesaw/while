sandwith_orders = ['cырный', 'рыбный', 'двойной', 'летний', 'с маслом']
finished_sandwith = []

while sandwith_orders:
    sandwith = sandwith_orders.pop()
    print(f'Заказали {sandwith} сэндвитч')
    finished_sandwith.append(sandwith)
print('\n')
for sandwith in finished_sandwith:
    print(f'Приготовили {sandwith} сэндвич')