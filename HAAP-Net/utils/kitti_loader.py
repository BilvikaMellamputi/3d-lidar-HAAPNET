import numpy as np
import torch

def load_kitti_lidar(file_path):
    """Loads a KITTI LiDAR point cloud (.bin) file"""
    points = np.fromfile(file_path, dtype=np.float32).reshape(-1, 4)  # (x, y, z, reflectance)
    return torch.tensor(points[:, :3], dtype=torch.float32)  # Only (x, y, z)

def load_kitti_labels(label_path):
    """Loads KITTI 3D object labels from .txt file"""
    labels = []
    with open(label_path, 'r') as f:
        for line in f:
            data = line.split()
            class_name = data[0]
            bbox_3d = np.array([float(data[i]) for i in range(8, 15)])  # 3D bounding box params
            labels.append((class_name, bbox_3d))
    return labels
