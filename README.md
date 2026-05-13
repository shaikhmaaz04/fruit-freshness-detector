# 🍎 Fruit Freshness Detection: Efficiency vs. Accuracy

## Project Overview

This project is a deep learning-based binary classification system designed to distinguish between **Fresh** and **Spoiled** fruit images. It also serves as a comparative study between a lightweight custom CNN architecture and a transfer learning-based ResNet-50 model, focusing on the trade-off between model size, inference speed, and prediction accuracy.

The application provides an interactive Streamlit interface for real-time image prediction, batch inference, and performance benchmarking.

---

## 🚀 Key Features

- **Dual-Architecture Support:** Switch between a custom **SimpleCNN** model and a pre-trained **ResNet-50** transfer learning model.
- **Batch Image Processing:** Perform inference on multiple uploaded images simultaneously.
- **Latency Benchmarking:** Displays total latency and average inference time per image.
- **Modern Streamlit UI:** Responsive drag-and-drop interface with image previews.
- **Transfer Learning Integration:** Fine-tuned ResNet-50 for high-accuracy classification.
- **Performance Comparison:** Compare lightweight vs deep architectures in real-world inference scenarios.

---

## 🌐 Live Streamlit Demo

> Replace the placeholder URL below with your deployed Streamlit application link.

```text
https://fruit-freshness-detector-cnn-tl.streamlit.app/
```

---

## 📸 Application Screenshots

### 🧠 ResNet-50 Interface

| Screenshot 1 | Screenshot 2 |
|---|---|
| ![ResNet50 Screenshot 1](assets/resnet50_1.png) | ![ResNet50 Screenshot 2](assets/resnet50_2.png) |

---

### ⚡ SimpleCNN Interface

| Screenshot 1 | Screenshot 2 |
|---|---|
| ![SimpleCNN Screenshot 1](assets/simplecnn_1.png) | ![SimpleCNN Screenshot 2](assets/simplecnn_2.png) |

---

## 📊 Model Comparison

| Metric | SimpleCNN (Custom CNN) | ResNet-50 (Transfer Learning) |
|---|---|---|
| **Model Size** | ~1.5 MB | ~90 MB |
| **Accuracy** | 98.83% | 98.12% |
| **Inference Latency** | ~30 ms / image | ~50 ms / image |
| **Architecture Type** | Lightweight CNN | Deep Residual Network |

---

## 🧠 Deep Learning Approaches

### 🔹 SimpleCNN
A lightweight custom convolutional neural network built from scratch using PyTorch.  
Optimized for:
- low latency
- smaller model size
- efficient deployment on edge devices

### 🔹 ResNet-50 Transfer Learning
A transfer learning approach using a pre-trained ResNet-50 backbone with a modified classification head for binary classification.

Benefits:
- stronger feature extraction
- improved generalization
- higher representational capacity

---

## 🛠️ Technology Stack

- **Deep Learning Framework:** PyTorch
- **Frontend/UI:** Streamlit
- **Image Processing:** Pillow (PIL), Torchvision
- **Programming Language:** Python
- **Version Control:** Git & Git LFS
- **Visualization:** Matplotlib

---

## 📦 Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/shaikhmaaz04/fruit-freshness-detector.git
cd fruit-freshness-detector
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Add Model Weights

Place the trained `.pt` files inside the `models/` directory:

```text
models/
├── cnn_fruit_model.pt
└── resnet50_fruit_model.pt
```

---

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 📓 Training Notebooks

The repository includes complete Jupyter notebooks covering:

- dataset preprocessing
- data augmentation
- CNN model training
- transfer learning with ResNet-50
- evaluation metrics
- prediction visualization
- performance benchmarking

### Included Notebooks

```text
notebooks/
├── Fresh_Harvest_Classification_CNN.ipynb
└── Fresh_Harvest_Classification_TL.ipynb
```

---

## 📁 Project Structure

```text
fruit-freshness-detector/
│
├── app.py                                # Streamlit application entry point
├── predictor.py                          # Model architectures & inference logic
├── requirements.txt                      # Project dependencies
├── runtime.txt                           # Python runtime version
├── README.md                             # Project documentation
├── .gitattributes                        # Git LFS configuration
├── .gitignore                            # Standard Python exclusions
│
├── assets/                               # Application screenshots
│   ├── resnet50_1.png
│   ├── resnet50_2.png
│   ├── simplecnn_1.png
│   └── simplecnn_2.png
│
├── notebooks/                            # Training & experimentation notebooks
│   ├── Fruit_Freshness_Classification_CNN.ipynb
│   └── Fruit_Freshness_Classification_TL.ipynb
│
└── models/                               # Trained model weights
    ├── cnn_fruit_model.pt
    └── resnet50_fruit_model.pt
```

---

## ⚙️ How the System Works

1. Upload one or multiple fruit images through the Streamlit interface.
2. Choose the desired inference model:
   - **SimpleCNN** for lightweight and faster predictions
   - **ResNet-50** for transfer learning-based classification
3. Uploaded images are automatically:
   - resized
   - normalized
   - converted into tensors
4. The selected model performs inference in batches.
5. Results displayed include:
   - predicted freshness status
   - confidence score
   - total inference latency
   - average inference time per image

---

## 📈 Performance Highlights

- Achieved over **98% classification accuracy** on both architectures.
- Implemented optimized batch inference for reduced latency.
- Compared lightweight CNNs against transfer learning models in deployment-oriented scenarios.
- Demonstrated practical trade-offs between:
  - model size
  - inference speed
  - predictive performance

---

## 🔮 Future Improvements

- Real-time webcam freshness detection
- Mobile deployment using TensorFlow Lite / ONNX
- Multi-class fruit categorization
- Cloud-based REST API deployment
- Model quantization for ultra-fast inference
- Larger and more diverse fruit datasets
- Explainable AI visualizations (Grad-CAM)

---

## ⚠️ Disclaimer

This project is intended solely for educational and research purposes.

- The dataset used for training is proprietary and not included in the repository.
- Predictions generated by this system should not be used for commercial food quality assurance systems.
- Model performance may vary depending on:
  - lighting conditions
  - camera quality
  - fruit variety
  - background complexity
- The creator is not responsible for misuse or incorrect interpretation of predictions.

---