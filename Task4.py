rev = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
if rev > costs:
    profit = rev - costs
    print(f'Финансовый результат - прибыль. Ее величина: {profit}')
    rent = profit / rev
    print(f'Рентабельность: {rent}')
    staff = int(input('Введите количество сотрудников: '))
    profit_staff = float(profit / staff)
    print(f'Прибыль фирмы в расчете на одного сотрудника: {profit_staff}')
else:
    print('Фирма работает в убыток')