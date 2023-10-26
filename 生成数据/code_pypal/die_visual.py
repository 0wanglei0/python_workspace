import pygal

from die import Die

die = Die()
die8 = Die(8)

results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

results8 = []
for roll_num in range(100):
    result = die8.roll()
    results8.append(result)
print(results8)

frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

frequencies8 = []
for value in range(1, die8.num_sides + 1):
    frequency = results8.count(value)
    frequencies8.append(frequency)

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
