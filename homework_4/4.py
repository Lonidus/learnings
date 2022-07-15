import simple_draw as sd
from homework_2.rainbow import rainbow
from homework_2.smile import smile
from homework_2.brick_wall import block_wall
from homework_3.snow import snowflakes
from homework_3.tree import draw_branches

sd.resolution = (1200, 800)
sd.rectangle(sd.get_point(0, 0), sd.get_point(1200, 100), color=sd.COLOR_ORANGE, width=0)


def house(point1, point2):
    block_wall(point1, point2)
    sd.line(sd.get_point(*point1), sd.get_point(point1[0], point2[1]), width=3)
    sd.line(sd.get_point(point2[0] + 25, point1[1]), sd.get_point(point2[0] + 25, point2[1]), width=3)
    roof_pointlist = [sd.get_point(point1[0] - 20, point2[1]),
                      sd.get_point((point2[0] + 25 + point1[0]) / 2, point2[1] + 70),
                      sd.get_point(point2[0] + 45, point2[1])
                      ]
    sd.polygon(roof_pointlist, color=sd.COLOR_RED, width=0)
    sd.square(sd.get_point(point2[0] - 100, point2[1] - 100), side=70, color=sd.COLOR_BLUE, width=0)
    sd.square(sd.get_point(point2[0] - 100, point2[1] - 100), side=70, color=sd.COLOR_WHITE, width=4)
    smile(point2[0] - 65, point2[1] - 65, color=sd.COLOR_YELLOW, radius=30)

sd.start_drawing()
rainbow(radius=900, point=sd.get_point(350, 100), width=10)
house((300, 100), (700, 300))
draw_branches(sd.get_point(1000, 100), angle=90, length=50)
draw_branches(sd.get_point(1100, 100), angle=90, length=50)
draw_branches(sd.get_point(900, 100), angle=90, length=50)
sd.finish_drawing()
snowflakes(40, (0, 110), (250, 700), 20)

sd.pause()
