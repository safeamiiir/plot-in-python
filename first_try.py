import python_plotter

print(f"python_plotter v{python_plotter.__version__}")

# Create a simple 3D scatter plot
x = [1, 2, 3, 4, 5]
y = [1, 4, 2, 3, 5]
z = [2, 1, 5, 3, 4]

# # Create and show the visualization
# fig = python_plotter.visualiser(x, y, z, title="My First 3D Plot")
# fig.show()

# Create a cube visualization
fig_cube = python_plotter.Figure()
fig_cube.update_layout(title="3D Cube Example", background_color="#2a2a2a")

# Add a solid cube
cube1 = python_plotter.Cube(
    x=0, y=0, z=0,
    size=2,
    color='#ff6b6b',
    name="Red Cube"
)

# Add a wireframe cube
cube2 = python_plotter.Cube(
    x=3, y=0, z=0,
    size=1.5,
    color='#4ecdc4',
    wireframe=True,
    name="Cyan Wireframe Cube"
)

# Add some scatter points around the cubes
scatter = python_plotter.Scatter3D(
    x=[-2, -1, 4, 5], 
    y=[2, -2, 2, -1], 
    z=[1, 1, 1, 2], 
    marker_color='#ffe66d',
    marker_size=0.1,
    name="Yellow points"
)

fig_cube.add_trace(cube1)
fig_cube.add_trace(cube2)
fig_cube.add_trace(scatter)
fig_cube.show()
