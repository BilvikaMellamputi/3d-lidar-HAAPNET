import open3d as o3d
import numpy as np
import cv2
import os

pcd_file = "lidar_point_cloud.pcd"  # Ensure this matches your .pcd filename

if not os.path.exists(pcd_file):
    print(f"Error: {pcd_file} not found. Please check the file path.")
    exit()

pcd = o3d.io.read_point_cloud(pcd_file)

vis = o3d.visualization.Visualizer()
vis.create_window(visible=False, width=1280, height=720)  # Explicit window size
vis.add_geometry(pcd)
vis.poll_events()
vis.update_renderer()

ctr = vis.get_view_control()
ctr.set_front([0, 0, -1])   # Set camera facing forward
ctr.set_lookat([0, 0, 0])   # Set the center of view at origin
ctr.set_up([0, -1, 0])      # Adjust "up" direction
ctr.set_zoom(0.5)           # Adjust zoom level

video_filename = "lidar_visualization.mp4"
fps = 30
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(video_filename, fourcc, fps, (1280, 720))

for _ in range(90): 
    vis.poll_events()
    vis.update_renderer()
    ctr.rotate(5.0, 0.0)  

    img = vis.capture_screen_float_buffer(do_render=True)
    img = (np.asarray(img) * 255).astype(np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR) 
    out.write(img)

out.release()
vis.destroy_window()
print(f"Video saved as {video_filename}")
###########################################################
import open3d as o3d
import numpy as np
import cv2
import os

pcd_file = "lidar_point_cloud.pcd"  

if not os.path.exists(pcd_file):
    print(f" Error: {pcd_file} not found. Please check the file path.")
    exit()

pcd = o3d.io.read_point_cloud(pcd_file)

vis = o3d.visualization.Visualizer()
vis.create_window(visible=False, width=1280, height=720)
vis.add_geometry(pcd)
vis.poll_events()
vis.update_renderer()

ctr = vis.get_view_control()
ctr.set_lookat([0, 0, 0])  # Set the center of rotation at the origin
ctr.set_up([0, -1, 0])     # Define the upward direction
ctr.set_zoom(0.5)          # Adjust zoom level

video_filename = "lidar_360_view.mp4"
fps = 30
num_frames = 180  # More frames for smoother rotation
angle_per_frame = 360 / num_frames  # Rotate evenly

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(video_filename, fourcc, fps, (1280, 720))

for i in range(num_frames):
    vis.poll_events()
    vis.update_renderer()
    ctr.rotate(angle_per_frame, 0.0)  # Rotate horizontally

    img = vis.capture_screen_float_buffer(do_render=True)
    img = (np.asarray(img) * 255).astype(np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    out.write(img)

out.release()
vis.destroy_window()
print(f"360° LiDAR video saved as {video_filename}")
