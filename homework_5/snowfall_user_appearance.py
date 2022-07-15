import simple_draw as sd
from snowfall import make_snowflakes, snowflakes_color, move_snowflakes, snowflake_at_ground_number, del_snowflakes
sd.resolution = (1200, 800)

make_snowflakes(20)
while True:
    count = 0
    snowflakes_color(color=sd.background_color)
    move_snowflakes()
    snowflakes_color(color=sd.COLOR_WHITE)
    if snowflake_at_ground_number():
        count += len(snowflake_at_ground_number())
        del_snowflakes(snowflake_at_ground_number())
        make_snowflakes(count)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
sd.pause()
