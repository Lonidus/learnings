import simple_draw as sd

sd.resolution = (1200, 800)


def rainbow(radius, point,width):
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    for color in rainbow_colors:
        sd.circle(center_position=point, radius=radius, color=color, width=width)
        radius += width


# rainbow(radius=900, point=sd.get_point(350, 100), width=10)
# sd.pause()
