my_family = ["мама", "бабушка", "папа"]
family_high = [164, 160, 181,]
my_family_high = [[family_high], [my_family] ]
print("Рост отца: ", family_high[2], "см")
print("Общий рост моей семьи: ", round(sum(family_high) / len(family_high)) , "см")