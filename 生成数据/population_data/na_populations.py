import pygal_maps_world.maps as maps

wm = maps.World()
wm.title = 'Populations of Countries in North America'
wm.add('North Ameraica', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
wm.render_to_file('na_populations.svg')
