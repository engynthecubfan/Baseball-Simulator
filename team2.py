import statistics
lineup = [93, 96, 98, 99, 96, 92, 91, 90, 1]
rotation = [99, 98, 97, 94, 91]
bullpen = [99, 98, 97, 96, 95, 94]
x = statistics.mean(lineup) + 9
y = statistics.mean(rotation) + 5
z = statistics.mean(bullpen) + 6
combined = x+y+z
ovr = 3+combined/3
