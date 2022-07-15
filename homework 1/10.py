goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
lamp_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
lamp_value = store[goods['Лампа']][0]['quantity']

table_cost = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price'] + store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']
table_value = store[goods['Стол']][0]['quantity'] + store[goods['Стол']][1]['quantity']

sofa_cost = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price'] + store[goods['Диван']][1]['quantity'] * store[goods['Диван']][1]['price']
sofa_value = store[goods['Диван']][0]['quantity'] + store[goods['Диван']][1]['quantity']

chair_cost = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price'] + store[goods['Стул']][1]['quantity'] * store[goods['Стул']][1]['price'] + store[goods['Стул']][2]['quantity'] * store[goods['Стул']][2]['price']
chair_value = store[goods['Стул']][0]['quantity'] + store[goods['Стул']][1]['quantity'] + store[goods['Стул']][2]['quantity']
print('Лампа -', lamp_value, 'шт, стоимость', lamp_cost, 'руб')
print('Стол -', table_value, 'шт, стоимость', table_cost, 'руб')
print('Диван -', sofa_value, 'шт, стоимость', sofa_cost, 'руб')
print('Стул -', chair_value, 'шт, стоимость', chair_cost, 'руб')

