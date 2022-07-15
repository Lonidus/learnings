import simple_draw as sd

sd.resolution = (1200, 800)
colors = [
    sd.COLOR_RED,
    sd.COLOR_ORANGE,
    sd.COLOR_YELLOW,
    sd.COLOR_GREEN,
    sd.COLOR_CYAN,
    sd.COLOR_BLUE,
    sd.COLOR_PURPLE,
]


def figure(point, sides, length, angle, color):
    for _ in range(sides):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw(color=color)
        point = v1.end_point
        angle += 180 - (sides - 2) / sides * 180


color = 1
print(type(color))
while color:
    print("Возможные цвета:\n 0 : red\n 1 : orange\n 2 : yellow\n 3 : green\n 4 : cyan\n 5 : blue\n 6 : purple  ")
    color = input("Введите желаемый цвет: ")
    if type(color) or 6 < color < 0 == str:
        color = input("Вы ввели неверный цвет, введите еще раз:")
    elif 0 <= color <= 6:
        point = sd.get_point(200, 100)
        figure(point, sides=3, length=100, angle=0, color=colors[int(color)])
        point = sd.get_point(800, 100)
        figure(point, sides=4, length=100, angle=0, color=colors[int(color)])
        point = sd.get_point(800, 500)
        figure(point, sides=5, length=100, angle=0, color=colors[int(color)])
        point = sd.get_point(200, 500)
        figure(point, sides=6, length=100, angle=0, color=colors[int(color)])

        break

sd.pause()
