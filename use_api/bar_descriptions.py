import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_lable_rotation=45, show_Legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['system-design-primer', 'awesome-python', 'tensorflow']

plot_dicts = [
    {'value': 1000, 'label': 'Description of primer'},
    {'value': 1123, 'label': 'awesome-python'},
    {'value': 1234, 'label': 'tensorflow'}
]

chart.add('', plot_dicts)
chart.render_to_file('bar_description.svg')
