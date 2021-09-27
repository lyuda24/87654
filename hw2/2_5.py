my_sales = [57.8, 46.51, 97, 75.64, 84.51, 57.94, 47, 53.80, 49.06, 67.52, 57.64, 79, 85.43, 65.09, 37.96]

# а
for sale in my_sales:
    rub = int(sale)
    kop = (sale - rub) * 100
    print(f'{rub} руб {kop:02.0f} коп', end=', ')

# b
print(id(my_sales))
my_sales.sort()
print(id(my_sales))
for sale in my_sales:
    rub = int(sale)
    kop = (sale - rub) * 100
    print(f'{rub} руб {kop:02.0f} коп', end = ', ')

# c
for sale in sorted(my_sales)[::-1]:
    rub = int(sale)
    kop = (sale - rub) * 100
    print(f'{rub} руб {kop:02.0f} коп', end=', ')

# d
for sale in sorted(my_sales)[::-1][:5]:
    rub = int(sale)
    kop = (sale - rub) * 100
    print(f'{rub} руб {kop:02.0f} коп', end=', ')
