# Brain-Tumor-MRI-Classification-Using-CNN
A Deep Learning-based Brain Tumor MRI Classification web application built with TensorFlow and Streamlit. The CNN model classifies MRI images into Glioma, Meningioma, No Tumor, and Pituitary, providing confidence scores and class probabilities through an interactive user interface.

# 🧠 Brain Tumor MRI Classification using Deep Learning

A Deep Learning-based web application that classifies Brain MRI images into four categories using a Convolutional Neural Network (CNN). The application is built with TensorFlow/Keras and deployed using Streamlit.

---

# 📌 Project Overview

This project uses a trained CNN model to classify MRI brain images into one of the following categories:

- Glioma
- Meningioma
- No Tumor
- Pituitary

Users can upload an MRI image through the Streamlit web interface, and the model predicts the tumor type along with the confidence score.

---

# 🚀 Features

✅ Upload MRI images (.jpg, .jpeg, .png)

✅ Deep Learning CNN Model

✅ Four-Class Classification

✅ Prediction Confidence Score

✅ Class Probability Visualization

✅ Interactive Streamlit User Interface

✅ Responsive Layout with Sidebar

---

# 📂 Dataset

Dataset Name:
Brain Tumor MRI Dataset

Classes:
- Glioma
- Meningioma
- No Tumor
- Pituitary

Image Size:
128 × 128 pixels

---

# 🧠 Model Architecture

The CNN model consists of:

- Conv2D
- ReLU Activation
- MaxPooling2D
- Conv2D
- MaxPooling2D
- Flatten
- Dense Layer
- Dropout
- Output Layer (Softmax)

Framework:
TensorFlow / Keras

---

# 📊 Model Performance

Training Accuracy:
89.18%

Input Shape:
128 × 128 × 3

Output Classes:
4

Loss Function:
Categorical Crossentropy

Optimizer:
Adam

Evaluation Metric:
Accuracy

---

# 🛠️ Technologies Used

- Python
- TensorFlow
- Keras
- Streamlit
- NumPy
- Pillow

---

# 📁 Project Structure

```
Brain_Tumor_Project/
│
├── app.py
├── brain_tumor_model.keras
├── requirements.txt
├── README.md
├── Testing/
└── Screenshots/
```

---


# ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

# 🖥️ Application Workflow

```
Upload MRI Image
        │
        ▼
Image Preprocessing
        │
        ▼
CNN Model Prediction
        │
        ▼
Predicted Tumor Type
        │
        ▼
Confidence Score
        │
        ▼
Class Probabilities
```

---

# 📸 Screenshots

## Home Page

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/a6ac33c8-61e2-4621-9796-bae01ff54e5a" />


---

## Uploaded MRI Image

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/81c8db80-20e4-4bbb-8c85-331676977a4b" />


---

## Prediction Result

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/acd1fc50-0441-4b90-9930-795f5608e14b" />


---

## Class Probabilities

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/ab64b571-1d8d-485b-9e56-80a5e5eb2e47" />


---

# 📦 Requirements

```
streamlit
tensorflow
numpy
pillow
```

Install using

```bash
pip install -r requirements.txt
```

---

# 👨‍💻 Author

Tamil Arasan

B.Tech Artificial Intelligence and Data Science

Machine Learning & Deep Learning Enthusiast

---

# 📜 License

This project is developed for educational and learning purposes.
