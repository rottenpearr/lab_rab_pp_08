km_data = []
price_data = []
all_data = []
n_km = 1
n_price = 1
n_all = 1

staff = int(input(f'Введите количество сотрудников: '))
print(f'Введите расстояния (в км): ')
for i in range(staff):
    km = 0
    km = int(input())
    km_data.append([km, str(i+1)])
print(f'Введите тарифы такси: ')
for i in range(staff):
    price = 0
    price = int(input())
    price_data.append([price, str(i+1)])

while n_km < len(km_data):
    for i in range(len(km_data) - n_km):
        if km_data[i] > km_data[i + 1]:
            km_data[i], km_data[i + 1] = km_data[i + 1], km_data[i]
    n_km += 1

while n_price < len(price_data):
    for i in range(len(price_data) - n_price):
        if price_data[i] < price_data[i + 1]:
            price_data[i], price_data[i + 1] = price_data[i + 1], price_data[i]
    n_price += 1

for i in range(staff):
    all_data.append([km_data[i], price_data[i]])

while n_all < len(all_data):
    for i in range(len(all_data) - n_all):
        if all_data[i][0][1] > all_data[i + 1][0][1]:
            all_data[i], all_data[i + 1] = all_data[i + 1], all_data[i]
    n_all += 1

for item in all_data:
    rubles = ''
    money = str(item[0][0] * item[1][0])
    if (money[-1] == '0' or money[-1] == '5' or money[-1] == '6' or money[-1] == '7' or money[-1] == '8' or
            money[-1] == '9'):
        rubles = 'рублей'
    elif money[-1] == '1':
        rubles = 'рубль'
    elif money[-1] == '2' or money[-1] == '3' or money[-1] == '4':
        rubles = 'рубля'
    print(f'{item[0][1]} сотрудник должен сесть в такси № {item[1][1]}\n'
          f'Директор должен заплатить: {money} {rubles}\n')
