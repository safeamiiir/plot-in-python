"""Python plotter Visualiser - A Three.js based 3D visualization library."""

import webbrowser
import tempfile
import os
from typing import List, Optional


class Figure:
    """A 3D figure that can contain multiple traces."""
    
    def __init__(self):
        self.traces = []
        self.title = ""
        self.background_color = "#000000"
    
    def add_trace(self, trace):
        """Add a trace (data series) to the figure."""
        self.traces.append(trace)
    
    def update_layout(self, title: str = "", background_color: str = "#000000"):
        """Update the layout of the figure."""
        if title:
            self.title = title
        self.background_color = background_color
    
    def show(self):
        """Display the figure in a web browser."""
        html_content = self._generate_html()
        
        # Create a temporary HTML file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            f.write(html_content)
            temp_path = f.name
        
        # Open in browser
        webbrowser.open('file://' + os.path.abspath(temp_path))
        
        print(f"Visualization opened in browser: file://{os.path.abspath(temp_path)}")
    
    def _generate_html(self) -> str:
        """Generate the HTML content with Three.js visualization."""
        # Generate trace data
        traces_js = []
        for trace in self.traces:
            traces_js.append(trace.generate_js())
        
        traces_code = '\n'.join(traces_js)
        
        # Use template approach to avoid f-string issues with JavaScript
        html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>__TITLE__</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background-color: __BGCOLOR__;
            font-family: Arial, sans-serif;
            overflow: hidden;
        }
        #container {
            width: 100vw;
            height: 100vh;
        }
        #title {
            position: absolute;
            top: 20px;
            left: 20px;
            color: white;
            font-size: 24px;
            z-index: 100;
        }
        #controls {
            position: absolute;
            top: 20px;
            right: 20px;
            color: white;
            z-index: 100;
            font-size: 12px;
        }
    </style>
</head>
<body>
    <div id="title">__TITLE__</div>
    <div id="controls">
        Mouse: Drag to rotate | Wheel: Zoom
    </div>
    <div id="container"></div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    
    <script>
        // Scene setup
        const scene = new THREE.Scene();
        scene.background = new THREE.Color('__BGCOLOR__');
        
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.getElementById('container').appendChild(renderer.domElement);
        
        // Simple mouse controls
        let isMouseDown = false;
        let mouseX = 0;
        let mouseY = 0;
        let cameraAngleX = 0;
        let cameraAngleY = 0;
        let cameraDistance = 10;
        
        renderer.domElement.addEventListener('mousedown', function(e) {
            isMouseDown = true;
            mouseX = e.clientX;
            mouseY = e.clientY;
        });
        
        document.addEventListener('mouseup', function() {
            isMouseDown = false;
        });
        
        document.addEventListener('mousemove', function(e) {
            if (isMouseDown) {
                const deltaX = e.clientX - mouseX;
                const deltaY = e.clientY - mouseY;
                
                cameraAngleX += deltaX * 0.01;
                cameraAngleY += deltaY * 0.01;
                
                // Limit vertical rotation
                cameraAngleY = Math.max(-Math.PI/2, Math.min(Math.PI/2, cameraAngleY));
                
                updateCameraPosition();
                
                mouseX = e.clientX;
                mouseY = e.clientY;
            }
        });
        
        renderer.domElement.addEventListener('wheel', function(e) {
            cameraDistance *= (e.deltaY > 0) ? 1.1 : 0.9;
            cameraDistance = Math.max(1, Math.min(100, cameraDistance));
            updateCameraPosition();
            e.preventDefault();
        });
        
        function updateCameraPosition() {
            camera.position.x = cameraDistance * Math.cos(cameraAngleY) * Math.cos(cameraAngleX);
            camera.position.y = cameraDistance * Math.sin(cameraAngleY);
            camera.position.z = cameraDistance * Math.cos(cameraAngleY) * Math.sin(cameraAngleX);
            camera.lookAt(0, 0, 0);
        }
        
        // Add axes helper
        const axesHelper = new THREE.AxesHelper(5);
        scene.add(axesHelper);
        
        // Add grid
        const gridHelper = new THREE.GridHelper(10, 10);
        scene.add(gridHelper);
        
        // Add traces
        __TRACES__
        
        // Position camera
        updateCameraPosition();
        
        // Animation loop
        function animate() {
            requestAnimationFrame(animate);
            renderer.render(scene, camera);
        }
        
        // Handle window resize
        window.addEventListener('resize', function() {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        });
        
        animate();
    </script>
</body>
</html>'''
        
        # Replace placeholders
        html = html_template.replace('__TITLE__', self.title or 'Python plotter Visualization')
        html = html.replace('__BGCOLOR__', self.background_color)
        html = html.replace('__TRACES__', traces_code)
        
        return html


class Scatter3D:
    """A 3D scatter plot trace."""
    
    def __init__(self, x: List[float], y: List[float], z: List[float], 
                 mode: str = 'markers', 
                 marker_color: str = '#ff6b6b',
                 marker_size: float = 0.1,
                 name: str = ""):
        self.x = x
        self.y = y
        self.z = z
        self.mode = mode
        self.marker_color = marker_color
        self.marker_size = marker_size
        self.name = name
    
    def generate_js(self) -> str:
        """Generate JavaScript code for this trace."""
        points_data = []
        for i in range(len(self.x)):
            points_data.append(f"new THREE.Vector3({self.x[i]}, {self.y[i]}, {self.z[i]})")
        
        points_str = ',\n            '.join(points_data)
        trace_id = str(id(self))
        
        return f'''
        // {self.name or 'Scatter3D trace'}
        const points_{trace_id} = [
            {points_str}
        ];
        
        const geometry_{trace_id} = new THREE.SphereGeometry({self.marker_size}, 8, 6);
        const material_{trace_id} = new THREE.MeshBasicMaterial({{ color: '{self.marker_color}' }});
        
        points_{trace_id}.forEach(point => {{
            const sphere = new THREE.Mesh(geometry_{trace_id}, material_{trace_id});
            sphere.position.copy(point);
            scene.add(sphere);
        }});
        '''


class Cube:
    """A 3D cube trace."""
    
    def __init__(self, x: float = 0, y: float = 0, z: float = 0,
                 size: float = 1,
                 color: str = '#4ecdc4',
                 wireframe: bool = False,
                 name: str = ""):
        self.x = x
        self.y = y
        self.z = z
        self.size = size
        self.color = color
        self.wireframe = wireframe
        self.name = name
    
    def generate_js(self) -> str:
        """Generate JavaScript code for this trace."""
        wireframe_prop = "true" if self.wireframe else "false"
        trace_id = str(id(self))
        
        return f'''
        // {self.name or 'Cube trace'}
        const geometry_{trace_id} = new THREE.BoxGeometry({self.size}, {self.size}, {self.size});
        const material_{trace_id} = new THREE.MeshBasicMaterial({{ 
            color: '{self.color}',
            wireframe: {wireframe_prop}
        }});
        const cube_{trace_id} = new THREE.Mesh(geometry_{trace_id}, material_{trace_id});
        cube_{trace_id}.position.set({self.x}, {self.y}, {self.z});
        scene.add(cube_{trace_id});
        '''


def visualiser(x: Optional[List[float]] = None, 
               y: Optional[List[float]] = None, 
               z: Optional[List[float]] = None,
               mode: str = 'markers',
               title: str = "Python plotter 3D Visualization") -> Figure:
    """
    Create a 3D visualization similar to Plotly.
    
    Args:
        x: List of x coordinates
        y: List of y coordinates  
        z: List of z coordinates
        mode: Display mode ('markers', 'lines', 'markers+lines')
        title: Title of the plot
    
    Returns:
        Figure object that can be displayed with .show()
    
    Example:
        >>> import python_plotter
        >>> x = [1, 2, 3, 4, 5]
        >>> y = [1, 4, 2, 3, 5] 
        >>> z = [2, 1, 5, 3, 4]
        >>> fig = python_plotter.visualiser(x, y, z, title="My 3D Plot")
        >>> fig.show()
    """
    fig = Figure()
    fig.update_layout(title=title)
    
    # If data is provided, create a default scatter plot
    if x is not None and y is not None and z is not None:
        trace = Scatter3D(x=x, y=y, z=z, mode=mode, name="Data")
        fig.add_trace(trace)
    
    return fig
