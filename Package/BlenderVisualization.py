import bpy
import math
import numpy as np

# Simulation parameters
fps = 24
duration = 5  # seconds
num_points = int(duration * fps) + 1  # number of frames

L = 10.0  # horizontal distance
h = 10.0  # peak height

points_list = [] # Points in space that hold the location of the rocket after each time step
angles_list = [] # Angles in which the rocket is in after each time step

# Convert both lists into numpy lists
points = np.array(points_list)
angles = np.array(angles_list)

filepath = "pathname.obj"  # adjust the path if needed
bpy.ops.import_scene.obj(filepath=filepath)

# Retrieve the imported object from the selected objects
imported_objects = bpy.context.selected_objects
if imported_objects:
    obj = imported_objects[0]
else:
    raise RuntimeError("No objects were imported. Check the filepath and file format.")
    
for i in range(len(points)):
    obj.location.x = points[i][0]
    obj.rotation_euler.x = math.radians(angles[i][0])
    obj.location.y = points[i][1]
    obj.rotation_euler.y = math.radians(angles[i][1])
    obj.location.z = points[i][2]
    obj.rotation_euler.z = math.radians(angles[i][2])
    obj.keyframe_insert("location", frame = i + 1)
    obj.keyframe_insert(data_path="rotation_euler", frame = i + 1)