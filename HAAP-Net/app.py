import streamlit as st
import open3d as o3d
import numpy as np
import os

st.title("🚗 HAAP-Net LiDAR Visualization")

# Upload a .pcd file
uploaded_file = st.file_uploader("Upload a LiDAR .pcd file", type=["pcd"])
if uploaded_file is not None:
    pcd_file = "uploaded_lidar.pcd"
    with open(pcd_file, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Load Point Cloud
    pcd = o3d.io.read_point_cloud(pcd_file)

    # Convert to NumPy for Display
    points = np.asarray(pcd.points)
    st.write(f"**Total Points in LiDAR Scan:** {len(points)}")

    # Display Interactive 3D LiDAR Visualization
    st.write("### Interactive 3D LiDAR View:")
    o3d.visualization.draw_geometries([pcd])

st.write("📌 Upload a KITTI .pcd file to visualize it in 3D!")
