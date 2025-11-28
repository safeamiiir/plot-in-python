import python_plotter

# Create a cube visualization
fig_cube = python_plotter.Figure()
fig_cube.update_layout(title="3D CNOT", background_color="#2a2a2a")

# Add a solid cube
cube1 = python_plotter.Cube(
    x=0, y=0, z=0,
    size=2,
    color='#ff6b6b',
    name="Red Cube"
)
# Add a solid cube
cube2 = python_plotter.Cube(
    x=0, y=2, z=0,
    size=2,
    color="#8e1d1d",
    name="2nd Red Cube"
)

# Add a cube stacked on top of cube2 (z-axis)
cube2_top = python_plotter.Cube(
    x=0, y=2, z=2,
    size=2,
    color="#5a0f0f",
    name="Cube on top of 2nd"
)

# Add another cube stacked on cube2_top (z-axis)
cube2_top2 = python_plotter.Cube(
    x=0, y=2, z=4,
    size=2,
    color="#3d0a0a",
    name="2nd cube on top"
)

# Add a cube extending from cube2_top2 along y-axis
cube2_top2_side = python_plotter.Cube(
    x=0, y=4, z=4,
    size=2,
    color="#2b0707",
    name="Cube extending from top"
)

# Add another cube extending further along y-axis
cube2_top2_side2 = python_plotter.Cube(
    x=0, y=6, z=4,
    size=2,
    color="#1f0505",
    name="2nd extending cube"
)

# Add a cube extending from cube2_top2_side2 in negative x-direction
cube2_top2_side2_nx1 = python_plotter.Cube(
    x=-2, y=6, z=4,
    size=2,
    color="#150404",
    name="1st negative x-axis extension"
)

# Add another cube extending further in negative x-direction
cube2_top2_side2_nx2 = python_plotter.Cube(
    x=-4, y=6, z=4,
    size=2,
    color="#0d0202",
    name="2nd negative x-axis extension"
)

# Build a 5-cube column next to cube2_top2_side2_nx2 along y-axis
cube_column2_1 = python_plotter.Cube(
    x=-4, y=0, z=4,
    size=2,
    color="#4a90e2",
    name="Column 2 - Cube 1"
)

cube_column2_2 = python_plotter.Cube(
    x=-4, y=2, z=4,
    size=2,
    color="#357abd",
    name="Column 2 - Cube 2"
)

cube_column2_3 = python_plotter.Cube(
    x=-4, y=4, z=4,
    size=2,
    color="#2a5d8a",
    name="Column 2 - Cube 3"
)

cube_column2_4 = python_plotter.Cube(
    x=-4, y=6, z=4,
    size=2,
    color="#1f4157",
    name="Column 2 - Cube 4"
)

cube_column2_5 = python_plotter.Cube(
    x=-4, y=8, z=4,
    size=2,
    color="#142a35",
    name="Column 2 - Cube 5"
)

# Add a solid cube
cube3 = python_plotter.Cube(
    x=0, y=4, z=0,
    size=2,
    color="#4ecdc4",
    name="3rd Cyan Cube"
)

# Add a solid cube
cube4 = python_plotter.Cube(
    x=0, y=6, z=0,
    size=2,
    color="#45b7d1",
    name="4th Blue Cube"
)

# Add a solid cube
cube5 = python_plotter.Cube(
    x=0, y=8, z=0,
    size=2,
    color="#96ceb4",
    name="5th Green Cube"
)

fig_cube.add_trace(cube1)
fig_cube.add_trace(cube2)
fig_cube.add_trace(cube2_top)
fig_cube.add_trace(cube2_top2)
fig_cube.add_trace(cube2_top2_side)
fig_cube.add_trace(cube2_top2_side2)
fig_cube.add_trace(cube2_top2_side2_nx1)
fig_cube.add_trace(cube2_top2_side2_nx2)
fig_cube.add_trace(cube_column2_1)
fig_cube.add_trace(cube_column2_2)
fig_cube.add_trace(cube_column2_3)
fig_cube.add_trace(cube_column2_4)
fig_cube.add_trace(cube_column2_5)
fig_cube.add_trace(cube3)
fig_cube.add_trace(cube4)
fig_cube.add_trace(cube5)
fig_cube.show()
