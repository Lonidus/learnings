# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)

flakes = []


class Snowflake:
    count = 0

    def __init__(self):
        self.position = [sd.randint(0, 1200), sd.randint(750, 780)]
        self.length = sd.randint(20, 30)

    def draw(self):
        sd.snowflake(sd.get_point(self.position[0], self.position[1]), length=self.length)

    def move(self):
        self.position[0] += sd.randint(-10, 10)
        self.position[1] -= sd.randint(5, 10)

    def can_fall(self):
        return self.position[1] > 0

    def get_fallen_flakes(self):
        if self.position[1] <= 0:
            self.count += 1
        return self.count


def get_flakes(N=1):
    return [Snowflake() for _ in range(N)]


flakes = get_flakes(20)
while True:
    sd.clear_screen()
    for flake in flakes:
        if flake.can_fall():
            flake.move()
            flake.draw()
        else:
            flakes.append(Snowflake())
            flakes.remove(flake)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
sd.pause()
