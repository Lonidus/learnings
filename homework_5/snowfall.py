import simple_draw as sd

snowflakes = []
snow_list_x, snow_list_y, snow_length = list(), list(), list()


def make_snowflakes(N):
    """Function makes list of snowflakes coordinates (x,y) and list of snowflakes length"""
    global snowflakes
    global snow_list_x, snow_list_y, snow_length
    for _ in range(N):
        snow_list_x.append(sd.random_number(0, 1200))
        snow_list_y.append(sd.random_number(800 - 50, 800))
        snow_length.append(sd.random_number(10, 50))
    snowflakes = [snow_list_x] + [snow_list_y] + [snow_length]


def snowflakes_color(color):
    for i in range(len(snowflakes[0])):
        sd.snowflake(sd.get_point(snowflakes[0][i], snowflakes[1][i]), color=color, length=snowflakes[2][i])


def move_snowflakes():
    for i in range(len(snowflakes[0])):
        snowflakes[0][i] += sd.random_number(-10, 10)
        snowflakes[1][i] -= sd.random_number(10, 15)


def snowflake_at_ground_number():
    numbers = []
    for i in range(len(snowflakes[1])):
        if snowflakes[1][i] < 0:
            numbers.append(i)
    return numbers


def del_snowflakes(numbers):
    a = 0
    while numbers:
        del snowflakes[0][numbers[0]]
        del snowflakes[1][numbers[0]]
        del snowflakes[2][numbers[0]]
        del numbers[0]
        if numbers:
            a -= 1
            numbers[0] += a
        else:
            break
