import statistics
lineup = [97, 98, 98, 99, 96, 95, 94, 93, 1]
rotation = [99, 94, 91, 87, 85]
bullpen = [95, 90, 84, 81, 79, 78]
x = statistics.mean(lineup) + 9
y = statistics.mean(rotation) + 5
z = statistics.mean(bullpen) + 6
combined = x+y+z
ovr = 3+combined/3