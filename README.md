# 3d-lidar-HAAPNET

### **📌 Here is your `README.md` file content:**  
Simply **copy and paste** this into your `README.md` file.

# 🚀 3D LiDAR HAAP-Net  

## 📌 Description  
This project implements an **interactive 3D LiDAR visualization** using **Three.js and Python (Open3D)**.  
It allows users to **view, rotate, zoom, and explore LiDAR point clouds** in a web browser.  

The project also includes a **deep learning model (HAAP-Net)** that processes **LiDAR data for 3D object detection** using:
- **Convolutional Neural Networks (CNNs)**
- **Graph Neural Networks (GNNs)**
- **Adaptive Attention Mechanisms**  

---

## 🌟 Features  
✔ **3D LiDAR Visualization** – Interactive point cloud rendering in a web browser  
✔ **Full 360° Rotation** – Users can rotate, zoom, and move the view freely  
✔ **AI-Based Object Detection** – HAAP-Net detects 3D objects in LiDAR scans  
✔ **LiDAR Data Processing** – Converts `.pcd` to JSON for web rendering  
✔ **Netlify Deployment** – Easily host the visualization online  


## 📁 Project Structure  
📂 HAAP-Net
 **├── 📂 models/            # Deep learning models (CNN + GNN)**
 **├── 📂 utils/             # LiDAR data loaders**
 **├── 📂 web/               # Frontend (Three.js + JSON)**
 **│   ├── index.html        # Interactive 3D visualization**
 **│   ├── web_data/         # JSON files for point cloud**
 **├── train.py              # Model training script**
 **├── test.py               # Model testing script**
 **├── video_generator.py    # Generates LiDAR visualization videos**
 **├── convert_pcd_to_json.py # Converts LiDAR PCD to JSON for web**
 **├── requirements.txt      # Python dependencies**
 **└── README.md             # Project documentation**


---

## 📜 Installation & Setup  

### 1️⃣ **Clone the Repository**  

git clone https://github.com/yourusername/HAAP-Net.git
cd HAAP-Net


### 2️⃣ **Install Dependencies**  

pip install -r requirements.txt
npm install -g netlify-cli  # If deploying to Netlify

### 3️⃣ **Convert LiDAR Data (PCD to JSON for Web)**  

python convert_pcd_to_json.py


### 4️⃣ **Run the Web Visualization Locally**  

cd web
python -m http.server 8000

🔗 Open in browser: `http://localhost:8000/`

### 5️⃣ **Deploy to Netlify**  

netlify deploy --prod

---

## 📌 Technologies Used  
🔹 **Python** – Data processing, AI model  
🔹 **Torch Geometric (GNNs)** – Graph Neural Network for 3D spatial learning  
🔹 **Open3D** – LiDAR point cloud manipulation  
🔹 **Three.js** – Web-based 3D visualization  
🔹 **Netlify** – Cloud deployment  

---

## 🌍 **Live Demo**  
🔗 **View Project Online:** [https://regal-jalebi-b77cbd.netlify.app/](https://regal-jalebi-b77cbd.netlify.app/)  


### **📌 How to Add This to GitHub?**
1️⃣ **Create `README.md` in your GitHub repository**  
2️⃣ **Paste the content above** into `README.md`  
3️⃣ **Commit and push the file**:
```bash
git add README.md
git commit -m "Added project documentation"
git push origin main
```

