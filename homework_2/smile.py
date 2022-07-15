import simple_draw as sd

sd.resolution = (1200, 800)


def smile(x, y, color, radius):
    """x, y - координаты центра. сolor - цвет"""

    point_list = [sd.get_point(x - radius * (45 / 100), y - radius * (25 / 100)),
                  sd.get_point(x - radius * (20 / 100), y - radius * (35 / 100)),
                  sd.get_point(x + radius * (20 / 100), y - radius * (35 / 100)),
                  sd.get_point(x + radius * (45 / 100), y - radius * (25 / 100))
                  ]
    point_head = sd.get_point(x, y)
    point_eye = sd.get_point(x - radius * (7 / 20), y + radius * (13 / 40))
    point_eye2 = sd.get_point(x + radius * (7 / 20), y + radius * (13 / 40))
    sd.circle(point_head, color=color, radius=radius)
    sd.circle(point_eye, color=color, radius=radius / 10)
    sd.circle(point_eye2, color=color, radius=radius / 10)
    sd.lines(point_list, color=color)


# for _ in range(10):
#     color = sd.random_color()
#     x, y = sd.random_number(100, 1100), sd.random_number(100, 700)
#     smile(x, y, color, radius=10)
# smile(200, 300, sd.COLOR_RED, 200)

# sd.pause()
