import torch
import torch.optim as optim
import torch.nn as nn
from models.haapnet import HAAPNet
from utils.kitti_loader import load_kitti_lidar, load_kitti_labels
from torch_geometric.nn import knn_graph  

# Load training data
train_lidar = load_kitti_lidar("data/training/velodyne/000000.bin")  # (N, 3)
train_labels = load_kitti_labels("data/training/label_2/000000.txt")  # (N, 3)

# Ensure LiDAR data is in correct shape for CNN
train_lidar = train_lidar.permute(1, 0).unsqueeze(0).unsqueeze(-1)  # (1, 3, N, 1)
print(f"train_lidar shape before model: {train_lidar.shape}")  # Debugging

# Initialize model
model = HAAPNet()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Forward pass through feature extractor to determine output size
with torch.no_grad():
    features = model.feature_extractor(train_lidar)
    num_output_points = features.shape[2]  # Correct number of points after downsampling

# Create labels that match the model output size
labels = torch.rand(num_output_points, 3)  # Match the downsampled size

# Training loop
for epoch in range(50):
    model.train()
    optimizer.zero_grad()

    # Generate a valid edge index
    num_neighbors = 5  # Adjust based on dataset
    edge_index = knn_graph(train_lidar.squeeze(0).squeeze(-1).permute(1, 0), k=min(num_neighbors, num_output_points - 1), loop=False)

    # Forward pass
    outputs = model(train_lidar, edge_index)

    # Ensure label size matches output size
    labels = labels[:outputs.shape[1], :]  # Trim if necessary

    # Debugging shapes before loss calculation
    print(f"outputs shape: {outputs.shape}")  # (batch_size, num_output_points, 3)
    print(f"labels shape: {labels.shape}")    # (num_output_points, 3)

    # Compute loss
    loss = criterion(outputs, labels)

    # Backpropagation
    loss.backward()
    optimizer.step()

    print(f"Epoch {epoch+1}: Loss = {loss.item():.4f}")

# Save trained model
torch.save(model.state_dict(), "haapnet_trained.pth")
print("Model training complete.")
print(f"train_lidar shape: {train_lidar.shape}")  # Should be (1, 3, N, 1)
print(f"edge_index shape: {edge_index.shape}")    # Should be (2, E) where E < N*N
