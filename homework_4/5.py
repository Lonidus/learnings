import simple_draw as sd
sd.resolution = (1200, 800)

sd.rectangle(sd.get_point(0, 0), sd.get_point(1200, 100), color=sd.COLOR_DARK_ORANGE, width=0)
sd.pause()