import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
import numpy as np

# ======================================================
# Page Configuration
# ======================================================

st.set_page_config(
    page_title="Brain Tumor MRI Classification",
    page_icon="🧠",
    layout="wide"
)

# ======================================================
# Load Model
# ======================================================

@st.cache_resource
def load_cnn():
    return load_model("brain_tumor_model.keras")

model = load_cnn()

class_names = [
    "Glioma",
    "Meningioma",
    "No Tumor",
    "Pituitary"
]

# ======================================================
# Sidebar
# ======================================================

st.sidebar.title("🧠 Model Information")

st.sidebar.markdown("### CNN Architecture")

st.sidebar.write("✔ Conv2D")
st.sidebar.write("✔ MaxPooling2D")
st.sidebar.write("✔ Flatten")
st.sidebar.write("✔ Dense")
st.sidebar.write("✔ Dropout")

st.sidebar.divider()

st.sidebar.metric("Input Size", "128 × 128")

st.sidebar.metric("Output Classes", "4")

st.sidebar.metric("Accuracy", "89.18 %")

st.sidebar.divider()

st.sidebar.info(
    """
This application classifies MRI Brain images into:

• Glioma

• Meningioma

• No Tumor

• Pituitary
"""
)

# ======================================================
# Header
# ======================================================

st.title("🧠 Brain Tumor MRI Classification")

st.markdown(
"""
### Deep Learning based Brain Tumor Detection

Upload an MRI scan and the trained CNN model will predict the tumor type.
"""
)
st.divider()

# -----------------------------
# Upload Image
# -----------------------------
uploaded_file = st.file_uploader(
    "📤 Upload MRI Image",
    type=["jpg", "jpeg", "png"]
)

# -----------------------------
# If Image Uploaded
# -----------------------------
if uploaded_file is not None:

    # Always convert uploaded image to RGB
    image_file = Image.open(uploaded_file).convert("RGB")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Uploaded MRI Image")

        st.image(image_file, use_container_width=True)

    with col2:

        st.subheader("Prediction")

        if st.button("Predict"):

            img = image_file.resize((128,128))

            img = image.img_to_array(img)

            img = img/255.0

            img = np.expand_dims(img, axis=0)

            prediction = model.predict(img)

            predicted_class = np.argmax(prediction)

            confidence = np.max(prediction)*100

            st.success(f"Prediction : {class_names[predicted_class]}")

            st.info(f"Confidence : {confidence:.2f}%")

            st.divider()

            st.subheader("Class Probabilities")

            for i in range(len(class_names)):

                probability = float(prediction[0][i])

                st.write(class_names[i])

                st.progress(probability)

                st.write(f"{probability*100:.2f}%")

# ======================================================
# Bottom Section
# ======================================================

st.divider()

st.subheader("📋 Model Details")

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric("Model","CNN")

with c2:
    st.metric("Input","128×128")

with c3:
    st.metric("Classes","4")

with c4:
    st.metric("Framework","TensorFlow")

st.divider()

st.caption(
    "Developed by Tamil Arasan | Brain Tumor MRI Classification using Deep Learning"
)
