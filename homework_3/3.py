import simple_draw as sd

sd.resolution = (1200, 800)


def figure(point, sides, length, angle):
    for _ in range(sides):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw()
        point = v1.end_point
        angle += 180 - (sides - 2) / sides * 180


point = sd.get_point(200, 100)

fig_type = 1
while fig_type:
    print("Возможные фигуры:\n 0 : треугольник\n 1 : квадрат\n 2 : пятиугольник\n 3 : шестиугольник ")
    fig_type = input("Введите желаемую фигуру: ")
    if fig_type.isdigit() is False:
        print("Вы ввели некорректный номер")
        continue
    elif int(fig_type) == 0:
        point = sd.get_point(200, 100)
        figure(point=point, sides=3, length=100, angle=0)
        break
    elif int(fig_type) == 1:
        point = sd.get_point(800, 100)
        figure(point=point, sides=4, length=100, angle=0),
        break
    elif int(fig_type) == 2:
        point = sd.get_point(800, 500)
        figure(point=point, sides=5, length=100, angle=0)
        break
    elif int(fig_type) == 3:
        point = sd.get_point(200, 500)
        figure(point=point, sides=6, length=100, angle=0)
        break
    print("Вы ввели некорректный номер")
sd.pause()
