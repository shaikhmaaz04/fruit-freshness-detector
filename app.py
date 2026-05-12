import streamlit as st
from PIL import Image
import torch
import os
import time
from predictor import FreshnessPredictor

st.set_page_config(page_title="Fruit AI - Detect Fruit Freshness", layout="wide")

st.sidebar.title("Model Settings")
model_option = st.sidebar.selectbox("Architecture", ("Simple CNN", "ResNet50"))
weight_files = {"Simple CNN": "models/cnn_fruit_model.pt", "ResNet50": "models/resnet50_fruit_model.pt"}
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

@st.cache_resource
def get_model(m_type, path):
    return FreshnessPredictor(m_type, path, device) if os.path.exists(path) else None

predictor = get_model(model_option, weight_files[model_option])

st.title("🍎 Fruit Freshness Detector")
uploaded_files = st.file_uploader("Upload fruit images (Single or Batch)...", 
                                  type=["jpg", "png", "jpeg"], 
                                  accept_multiple_files=True)

if uploaded_files and predictor:
    if st.button("Run Classification"):
        images = [Image.open(f).convert('RGB') for f in uploaded_files]
        
        with st.spinner(f"Analyzing {len(images)} sample(s)..."):
            start_time = time.time()
            results = predictor.predict(images)
            end_time = time.time()
            
            total_time = (end_time - start_time) * 1000
            time_per_img = total_time / len(images)

        # 1. Display Results Grid First
        st.write("### Predictions")
        cols = st.columns(4) 
        for idx, (img, label) in enumerate(zip(images, results)):
            with cols[idx % 4]:
                color = "green" if label == "Fresh" else "red"
                st.image(img, width='stretch')
                st.markdown(f"**:{color}[{label}]**")
        
        # 2. Display Metrics at the Bottom
        st.divider()
        st.write("### Performance Metrics")
        m_col1, m_col2, m_col3 = st.columns(3)
        m_col1.metric("Batch Size", len(images))
        m_col2.metric("Total Latency", f"{total_time:.2f} ms")
        m_col3.metric("Avg per Image", f"{time_per_img:.2f} ms")

elif not predictor:
    st.error("Critical Error: Model weights not found.")