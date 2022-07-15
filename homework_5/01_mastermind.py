from mastermind_engine import take_number, number_check

take_number()
counter = 0
while True:
    user_number = input("Введи число: ")
    counter += 1
    print(number_check(user_number))
    if list(number_check(user_number).values())[0] == 4:
        print("Вы угадали /^(._.)^/! Количество шагов: ", counter)
        one_more_time = input("Хотите еще партию? y/n ")
        if one_more_time == "y":
            counter = 0
            take_number()
        else:
            break
