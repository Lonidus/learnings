from random import shuffle


_number = []

def take_number():
    global _number
    _number = []
    list_of_variants = [0,1,2]
    for i in range(10):
        list_of_variants.append(i)
    shuffle(list_of_variants)
    for i in list_of_variants:
        if _number[0] == 0:
            _number.pop(0)
            _number.append(list_of_variants[5])
        if len(_number) == 4:
            break
        else:
            _number.append(i)


def number_check(user_number):
    bulls, cows = 0, 0
    for i in range(len(user_number)):
        if int(user_number[i]) == _number[i]:
            bulls += 1
        elif int(user_number[i]) in _number:
            cows += 1
    res = dict(bulls=bulls, cows=cows)
    return res
