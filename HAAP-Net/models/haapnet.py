import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import GCNConv

# Multi-Scale Feature Extraction
class MultiScaleFeatureExtractor(nn.Module):
    def __init__(self, in_channels=3):
        super(MultiScaleFeatureExtractor, self).__init__()
        self.conv1 = nn.Conv2d(in_channels, 32, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=2, padding=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, stride=2, padding=1)

    def forward(self, x):
        if x.dim() == 2:  # If input is (N, 3), reshape it
            x = x.permute(1, 0).unsqueeze(0).unsqueeze(-1)  # Convert to (batch, channels, height, width)

        x1 = F.relu(self.conv1(x))
        x2 = F.relu(self.conv2(x1))
        x3 = F.relu(self.conv3(x2))

        # Reshape for GNN compatibility (batch_size, features, num_points)
        x3 = x3.view(x3.shape[0], x3.shape[1], -1)
        return x3


# Graph Neural Network for Spatial Relations
class GNNSpatialModule(nn.Module):
    def __init__(self, in_features=128, out_features=64):
        super(GNNSpatialModule, self).__init__()
        self.conv1 = GCNConv(in_features, 128)
        self.conv2 = GCNConv(128, out_features)

    def forward(self, x, edge_index):
        num_nodes = x.shape[1]  # Number of points after feature extraction
        if edge_index.max() >= num_nodes:
            print(f"Warning: edge_index contains values outside valid range (max index: {edge_index.max()}, num_nodes: {num_nodes})")
            edge_index = edge_index.clamp(max=num_nodes - 1)  # Fix invalid indices
        
        x = x.permute(0, 2, 1).squeeze(-1)  # Convert to (batch, num_nodes, features)
        x = F.relu(self.conv1(x, edge_index))
        x = F.relu(self.conv2(x, edge_index))
        return x


# Adaptive Attention
class AdaptiveAttention(nn.Module):
    def __init__(self, in_features=64):
        super(AdaptiveAttention, self).__init__()
        self.attention = nn.Linear(in_features, 1)

    def forward(self, x):
        weights = torch.sigmoid(self.attention(x))
        return x * weights


# HAAP-Net Model
class HAAPNet(nn.Module):
    def __init__(self):
        super(HAAPNet, self).__init__()
        self.feature_extractor = MultiScaleFeatureExtractor()
        self.gnn = GNNSpatialModule()
        self.attention = AdaptiveAttention()
        self.fc = nn.Linear(64, 3)  # Output: (x, y, z)

    def forward(self, point_cloud, edge_index):
        features = self.feature_extractor(point_cloud)
        gnn_output = self.gnn(features, edge_index)
        attended_features = self.attention(gnn_output)
        output = self.fc(attended_features)
        return output
