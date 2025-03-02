import torch
from models.haapnet import HAAPNet
from utils.kitti_loader import load_kitti_lidar
from torch_geometric.nn import knn_graph
import open3d as o3d
import numpy as np
import threading

test_lidar = load_kitti_lidar("data/testing/velodyne/000001.bin")  
test_lidar = test_lidar.permute(1, 0).unsqueeze(0).unsqueeze(-1)  # Reshape

model = HAAPNet()
model.load_state_dict(torch.load("haapnet_trained.pth", weights_only=True))  # Prevent warning
model.eval()

num_neighbors = 5
edge_index = knn_graph(test_lidar.squeeze(0).squeeze(-1).permute(1, 0), k=num_neighbors, loop=False)

with torch.no_grad():
    predictions = model(test_lidar, edge_index)

print("Predicted 3D Object Centers:")
print(predictions)

points = test_lidar.squeeze().permute(1, 0).cpu().numpy()
predictions_np = predictions.squeeze().cpu().numpy()

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)

pcd = pcd.voxel_down_sample(voxel_size=0.1)

def visualize():
    vis = o3d.visualization.Visualizer()
    vis.create_window()
    vis.add_geometry(pcd)
    vis.run()  # Interactive window
    vis.destroy_window()

vis_thread = threading.Thread(target=visualize)
vis_thread.start()
