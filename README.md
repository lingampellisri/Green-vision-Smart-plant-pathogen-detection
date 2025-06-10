# 🌿 GreenVision: Smart Plant Pathogen Detection

A deep learning–powered web application for **early and accurate plant disease detection** using image analysis. Built with **Python**, **TensorFlow**, **CNN**, **OpenCV**, **Flask**, and **MongoDB**, this solution leverages AI to help farmers and agriculturalists detect crop infections from leaf images in real time.


---

## 🧠 Features

- 🔍 Detects and classifies **10+ plant diseases** (e.g., Tomato, Potato, Apple, Mango, Paddy).
- 🧠 Trained CNN model with **high accuracy** using image data.
- 🖼️ OpenCV-powered image preprocessing.
- 🌐 Real-time predictions via Flask web interface.
- 🔐 Login/Signup authentication with **MongoDB**.
- 📈 Clean UI for uploading leaf images and viewing results.

---

## 🖥️ Tech Stack

| Layer         | Technologies Used                        |
|---------------|------------------------------------------|
| AI/ML         | Python, TensorFlow, Keras (CNN)          |
| Image Handling| OpenCV, NumPy                            |
| Web Framework | Flask                                    |
| Frontend      | HTML5, CSS3, JavaScript                  |
| Database      | MongoDB (User Auth)                      |
| Deployment    | (Optional: Docker/Heroku/Vercel)         |

---

## 🧪 Supported Classes

The model has been trained to detect diseases in the following **10 plant types**:

- 🍅 Tomato
- 🥔 Potato
- 🍎 Apple
- 🥭 Mango
- 🌾 Paddy
- 🌽 Corn
- 🍇 Grape
- 🍊 Citrus
- 🍓 Strawberry
- 🌿 Healthy (Non-infected)

---

## 📂 Project Structure

Green-vision-Smart-plant-pathogen-detection/
├── LoginSignup/
│ └── loginsignup/
│ ├── templates/
│ │ ├── login.html
│ │ ├── signup.html
│ │ └── result.html
│ ├── static/
│ │ └── styles.css
│ ├── app.py # Main Flask app
│ ├── model.h5 # Trained CNN model
│ ├── mongo_setup.py # MongoDB connection
│ ├── utils.py # Preprocessing logic
├── dataset/
│ └── (image data by class)
├── train_model/
│ ├── preprocess.py # Augmentation & resize
│ ├── train.py # Model training script
│ ├── evaluate.py # Accuracy & loss metrics
├── README.md
├── requirements.txt
└── .gitignore



---

## ⚙️ How to Run Locally

### 🔧 Prerequisites

- Python 3.8+
- pip
- MongoDB installed or MongoDB Atlas URI
- Virtual environment (recommended)

### 📥 Installation

```bash
# Clone the repo
git clone https://github.com/<your-username>/Green-vision-Smart-plant-pathogen-detection.git
cd Green-vision-Smart-plant-pathogen-detection/LoginSignup/loginsignup

# Create virtual environment
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
▶️ Run the App

python app.py
Go to: http://127.0.0.1:5000

📊 Model Overview
📐 Architecture: 4 Convolutional Layers + MaxPooling + Dropout + Fully Connected Layers

🎯 Loss Function: Categorical Crossentropy

🧪 Optimizer: Adam

✅ Test Accuracy: ~96%

🖼️ Image Size: 224x224 (RGB)

🔐 Authentication Module
🆕 User Signup & Login

🔐 Passwords stored securely (bcrypt hashing)

📁 Optional: User prediction history

📦 Dataset
Publicly available PlantVillage dataset used, with custom filtering and cleaning:

Image augmentation (rotation, flips)

Noise removal using Gaussian Blur

Class balancing

🌱 Future Enhancements
📲 Android/iOS Mobile App

☁️ Cloud deployment with GPU acceleration

🧬 Add more plant classes & real-time camera capture

🛰️ IoT integration for smart farming systems

🤝 Contributing
We welcome contributions from the open-source community!


# Fork the repo
# Create your branch: git checkout -b feature-name
# Commit your changes: git commit -m 'Add new feature'
# Push to the branch: git push origin feature-name
# Open a Pull Request
📜 License
This project is licensed under the MIT License.

👨‍💻 Author
Navanitha Pothuganti
📧 pothugantinavanithareddy29@gmail.com 
🔗 linkedin.com/in/pothuganti-navanitha-73a119301
🔗 github.com/PothugantiNavanitha 

🌾 GreenVision: Empowering Agriculture with AI – One Leaf at a Time.
