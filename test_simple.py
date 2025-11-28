import python_plotter

# Simple test
fig = python_plotter.Figure()
fig.update_layout(title="Simple Test")

# Add a cube
cube = python_plotter.Cube(x=0, y=0, z=0, size=1, color='#ff0000')
fig.add_trace(cube)

fig.show()
