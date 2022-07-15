# envelop_x, envelop_y = 10, 7
# paper_x, paper_y = 11, 9
# if envelop_x >= paper_x and envelop_y >= paper_y:
#     print("Влезет")
# elif envelop_x >= paper_y and envelop_y >= paper_x:
#     print("Влезет")
# else:
#     print('Не влезет')
hole_x, hole_y = 8, 9
brick_x, brick_y, brick_z = 11, 3, 6
if (hole_x >= brick_x and hole_y >= brick_y) or (hole_x >= brick_y and hole_y >= brick_z) or (
        hole_x >= brick_x and hole_y >= brick_z):
    print("Влезет")
else:
    print("Не влезет")
