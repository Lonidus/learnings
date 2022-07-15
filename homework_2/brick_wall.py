import simple_draw as sd

# x1, y1 = 100, 0
sd.resolution = (1200, 800)


# start_point = sd.get_point(x, y)
# end_point = sd.get_point(x, y)
# for block_height in range(0, 801, 50):
#     for block_length in range(0, 1201, 100):
#         sd.line(sd.get_point(0, 0), sd.get_point(0, 50), color=sd.COLOR_RED, width=1)
#         sd.line(sd.get_point(0, 50), sd.get_point(100, 50), color=sd.COLOR_RED, width=1)
#         sd.line(sd.get_point(100, 50), sd.get_point(100, 0),
#                 color=sd.COLOR_RED, width=1)
#         sd.line(sd.get_point(100, 0), sd.get_point(0, 0), color=sd.COLOR_RED,
#                 width=1)
# for block_height in range(0, 801, 50):
#     for block_length in range(0, 1201, 100):
#         sd.line(sd.get_point(block_length, block_height), sd.get_point(block_length, block_height + 50), color=sd.COLOR_RED, width=1)
#         sd.line(sd.get_point(0, 50), sd.get_point(100, 50), color=sd.COLOR_RED, width=1)
#         sd.line(sd.get_point(100, 50), sd.get_point(100, 0),
#                 color=sd.COLOR_RED, width=1)
#         sd.line(sd.get_point(100, 0), sd.get_point(0, 0), color=sd.COLOR_RED,
#                 width=1)
def block_wall(point, point2, ):
    for block_height in range(point[1], point2[1], 50):
        for block_length in range(point[0], point2[0], 50):
            sd.rectangle(sd.get_point(block_length, block_height), sd.get_point(block_length + 50, block_height + 25),
                         width=1)
            sd.rectangle(sd.get_point(block_length + 25, block_height + 25),
                         sd.get_point(block_length + 75, block_height + 50), width=1)


# block_wall(point=(100, 50), point2=(300, 600))
#
# sd.pause()
