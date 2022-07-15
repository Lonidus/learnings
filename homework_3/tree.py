import simple_draw as sd

sd.resolution = (1200, 800)
point_0 = sd.get_point(300, 30)
angle_0 = 60
length_0 = 100


def draw_branches(point, angle, length, stick_color=0):
    if stick_color == 0:
        stick_line = sd.get_vector(start_point=point, angle=angle, length=length, width=4)
        stick_line.draw(color=sd.COLOR_DARK_ORANGE)
        point = stick_line.end_point
        length = length * 0.75
    if length < 2 or sd.user_want_exit():
        return
    next_length = length * 0.75
    left_angle = angle + 30
    stick_color += 1
    if stick_color <= 6:
        left_line = sd.get_vector(start_point=point, angle=left_angle, length=length, width=4)
        left_line.draw(color=sd.COLOR_DARK_ORANGE)
    else:
        left_line = sd.get_vector(start_point=point, angle=left_angle, length=length, )
        left_line.draw(color=sd.COLOR_GREEN)
    next_point = left_line.end_point
    draw_branches(point=next_point, angle=left_angle, length=next_length, stick_color=stick_color)

    right_angle = angle - 30
    if stick_color <= 6:
        right_line = sd.get_vector(start_point=point, angle=right_angle, length=length, width=4)
        right_line.draw(color=sd.COLOR_DARK_ORANGE)
    else:
        right_line = sd.get_vector(start_point=point, angle=right_angle, length=length, )
        right_line.draw(color=sd.COLOR_GREEN)
    next_point = right_line.end_point

    draw_branches(point=next_point, angle=right_angle, length=next_length, stick_color=stick_color)



# draw_branches(point=point_0, angle=angle_0, length=100)

# sd.pause()
