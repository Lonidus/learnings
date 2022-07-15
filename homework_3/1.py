import simple_draw as sd

sd.resolution = (1200, 800)
point = sd.get_point(300, 300)


# def figure_trio(point, angle, length):
#     for _ in range(3):
#         vector1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#         vector1.draw()
#         angle += 120
#         point = vector1.end_point
#
# def figure_qud(point, angle, length):
#     for _ in range(4):
#         vector1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#         vector1.draw()
#         angle += 90
#         point = vector1.end_point

# def figure_5(point, angle, length):
#     for _ in range(5):
#         vector1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#         vector1.draw()
#         angle += 60
#         point = vector1.end_point

# def figure_6(point, angle, length):
#     for _ in range(6):
#         vector1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#         vector1.draw()
#         angle += 72
#         point = vector1.end_point
#
# def fig(point, sides, length, angle, width):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
#     v1.draw()
#     angle += 180 - (sides - 2) / sides * 180
#     point = v1.end_point
#     return point, angle

def figure(point, sides, length, angle):
    for _ in range(sides):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw()
        point = v1.end_point
        angle += 180 - (sides - 2) / sides * 180
        print(point)


figure(point, sides=10, length=100, angle=0)

sd.pause()
