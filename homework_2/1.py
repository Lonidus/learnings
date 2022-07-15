user_input = input("Введите, пожалуйста, номер месяца: ")
days = {
    28: [
        {2: "Февраль"},
    ],
    30: [
        {4: "Апрель", 6: "Июнь", 9: "Сентябрь", 11: "Ноябрь"},
    ],
    31:
        [
            {1: "Январь", 3: "Март", 5: "Май", 7: "Июлю", 8: "Август", 10: "Октябрь", 12: "Декабрь"},
        ],
}
if int(user_input) > 12 or int(user_input) <= 0:
    print("Некорректное число")
if int(user_input) in days[28][0]:
    print("В месяце ", days[28][0][int(user_input)], "28 дней")
elif int(user_input) in days[30][0]:
    print("В месяце ", days[30][0][int(user_input)], "30 дней")
elif int(user_input) in days[31][0]:
    print("В месяце ", days[31][0][int(user_input)], "31 день")
