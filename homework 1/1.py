radius = 42
pi = 3.1415926
point_2 = (30, 30)
point = (23, 34)
square = pi * radius ** 2
print(round(square, 4))
point_radius = (point[0] ** 2 + point[1] ** 2) ** 0.5
print(point_radius <= radius)
point_radius_2 = (point_2[0] ** 2 + point_2[1] ** 2) ** 0.5
print(point_radius_2 <= radius)

