zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
birds = ['rooster', 'ostrich', 'lark', ]
zoo.insert(1, "bear")
print(zoo)
zoo.extend(birds)
print(zoo)
zoo.remove("elephant")
print(zoo)
print(zoo[0], " сидит в клетке # ", zoo.index("lion") )
print(zoo[6], " сидит в клетке # ", zoo.index("lark") )