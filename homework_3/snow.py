import simple_draw as sd

# x, y = 0, 0
# point = sd.get_point(x, y)
sd.resolution = (1200, 800)
N = 20


def snowflakes(N, point1, point2, max_size):
    """N - amount of snowlakes, point1 and point2 - left down angle limit and right upper angle limit, max size -
    maximum size of the flake """
    snow_listX, snow_listY, snow_length = list(), list(), list()
    for _ in range(N):
        snow_listX.append(sd.random_number(point1[0], point2[0]))
        snow_listY.append(sd.random_number(point2[1] - 50, point2[1]))
        snow_length.append(sd.random_number(10, max_size))
    result = [snow_listX] + [snow_listY] + [snow_length]
    print(result)
    while True:
        for i in range(N):
            if result[1][i] <= point1[1]:
                point = sd.get_point(result[0][i], result[1][i])
                sd.snowflake(point, length=result[2][i], color=sd.COLOR_WHITE)
                del result[0][i], result[1][i], result[2][i]
                result[0].append(sd.random_number(point1[0], point2[0]))
                result[1].append(sd.random_number(point2[1] - 50, point2[1]))
                result[2].append(sd.random_number(10, max_size))
                continue
            point = sd.get_point(result[0][i], result[1][i])
            sd.snowflake(point, length=result[2][i], color=sd.COLOR_WHITE)

        sd.sleep(.05)
        for i in range(N):
            if result[1][i] <= point1[1]:
                continue
            point = sd.get_point(result[0][i], result[1][i])
            sd.snowflake(point, length=result[2][i], color=sd.background_color)
            result[1][i] -= sd.random_number(0, 15)
            result[0][i] -= sd.random_number(-20, 20)

        if sd.user_want_exit():
            break


snowflakes(N, (100, 200), (1000, 600), max_size=30)
# sd.pause()
