import pygal

from die import Die

die = Die(8)
die8 = Die(8)

results = [die.roll() for i in range(1000)]
results8 = [die8.roll() for j in range(1000)]
print(results8)

frequencies = [results.count(value) for value in range(1, die.num_sides + 1)]
frequencies8 = [results8.count(value) for value in range(1, die8.num_sides + 1)]
#
# frequencies8 = []
# for value in range(1, die8.num_sides + 1):
#     frequency = results8.count(value)
#     frequencies8.append(frequency)

hist = pygal.Bar()
print(frequencies8)
print(frequencies)

hist.title = "Results of Rolling one D6 1000 times"
hist.x_labels = [str(num) for num in range(1, die8.num_sides + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6', frequencies)
hist.add('D8', frequencies8)
print("here")
hist.render_to_file('die_visual.svg')
