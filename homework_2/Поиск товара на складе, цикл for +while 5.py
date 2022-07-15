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
summ = 0
value = 0
for code in goods:
    for staff in store:
        i = len(store[goods[code]]) - 1
        if goods[code] == staff:
            while i > -1:
                summ = summ + (store[goods[code]][i]["quantity"])
                value = value + (store[goods[code]][i]["price"])
                i -= 1
            else:
                print("Количество ", code, " на складе: ", value, "штук,", " сумма: ", summ, " рублей")
                summ = 0
                value = 0

