shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}
sweets = {
    'печенье': [
        {'shop': 'ашан', 'price': 10.99},
        {'shop': 'пятерочка', 'price': 9.99},
        {'shop': 'магнит', 'price': 11.99}
    ],
    "конфеты": [
        {'shop': 'ашан', 'price': 34.99},
        {'shop': 'пятерочка', 'price': 32.99},
        {'shop': 'магнит', 'price': 30.99}
    ],
    "карамель": [
        {'shop': 'ашан', 'price': 45.99},
        {'shop': 'пятерочка', 'price': 46.99},
        {'shop': 'магнит', 'price': 41.99}
    ],
    "пирожное": [
        {'shop': 'ашан', 'price': 67.99},
        {'shop': 'пятерочка', 'price': 59.99},
        {'shop': 'магнит', 'price': 62.99}
    ],
    "морожное": [
        {'shop': 'ашан', 'price': 15.99},
        {'shop': 'пятерочка', 'price': 14.99},
        {'shop': 'магнит', 'price': 11.99}
    ]
}
biscuit_min_price = min(sweets['печенье'][0]["price"], sweets['печенье'][1]["price"], sweets['печенье'][2]["price"])
sweets_min_price = min(sweets['конфеты'][0]["price"], sweets['конфеты'][1]["price"], sweets['конфеты'][2]["price"])
cake_min_price = min(sweets['пирожное'][0]["price"], sweets['пирожное'][1]["price"], sweets['пирожное'][2]["price"])
ice_cream_min_price = min(sweets['морожное'][0]["price"], sweets['морожное'][1]["price"], sweets['морожное'][2]["price"])
print(biscuit_min_price)
print(sweets_min_price)
print(cake_min_price)
print(ice_cream_min_price)