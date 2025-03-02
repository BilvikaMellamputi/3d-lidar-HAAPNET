import numpy as np
import open3d as o3d

# Change this to your actual .bin file path
bin_file = "data/training/velodyne/000000.bin"
pcd_file = "lidar_point_cloud.pcd"

# Load .bin file (KITTI format)
point_cloud = np.fromfile(bin_file, dtype=np.float32).reshape(-1, 4)  # (X, Y, Z, Intensity)

# Convert to Open3D format
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(point_cloud[:, :3])  # Use only (X, Y, Z)

# Save as .pcd file
o3d.io.write_point_cloud(pcd_file, pcd)

print(f"✅ Converted {bin_file} to {pcd_file}")
