## 💡 **ML\_Projects**

This repository contains a curated collection of machine learning and AI-based mini-projects built using Python. Each project focuses on solving real-world problems using modern tools, libraries, and frameworks. The goal is to explore end-to-end ML and AI workflows—from data preparation to deployment-ready applications.

---

## ✅ **README for ML Projects**

## 📚 List of Projects

1. **[GPT-3.5 ChatBot using Streamlit](#1-gpt-35-chatbot-using-streamlit)**
   An interactive AI-powered chatbot app that leverages OpenAI's GPT-3.5 model with a Streamlit UI.

2. **[Object Detector using OpenCV and TensorFlow](#2-object-detector-using-opencv-and-tensorflow)**
   A real-time object detection system that identifies and localizes objects in video streams using the SSD MobileNet model.

*(More projects will be added soon...)*

---

## 📦 Projects Overview

---

### 🧠 1. GPT-4o ChatBot using Streamlit

> #### 📖 Project Description
>
> This project implements an AI chatbot using **OpenAI's GPT-4o model** within a **Streamlit** web interface. It handles real-time user queries, maintains session-based chat history, and responds conversationally. The app is lightweight and well-suited for experimenting with LLM integration.

> #### 🧰 Tech Stack / Tools Used
>
> * **Programming Language**: Python 3
> * **Libraries**: Streamlit, OpenAI, JSON, OS
> * **IDE**: VS Code / Jupyter Notebook
> * **API**: OpenAI GPT-4o
> * **Deployment**: Localhost or Streamlit Cloud

> #### 🚀 Features
>
> * Responsive chatbot interface
> * Persistent chat memory with Streamlit session state
> * API key securely read from a `config.json` file
> * GPT-4o integration via `GITHUB.ChatCompletio`
> * Simple and elegant user interface using Streamlit

> #### 🗂️ File Structure
>
> ```
> chatbot/
> │
> ├── app.py               # Streamlit app
> ├── config.json          # Contains API key (excluded from version control)
> ```

> #### ⚙️ How to Run
>
> 1. Clone the repository:
>
>    ```bash
>    git clone https://github.com/Ayusohm432/ML_Projects.git
>    cd ML_Projects/chatbot
>    ```
> 2. Create `config.json` with your GITHUB API key:
>
>    ```json
>    {
>      "GITHUB_API_KEY": "your-api-key-here"
>    }
>    ```
> 3. Install dependencies:
>
>    ```bash
>    pip install streamlit openai
>    ```
> 4. Launch the app:
>
>    ```bash
>    streamlit run app.py
>    ```

> #### 📌 Future Improvements
>
> * Add voice input/output
> * Add multiple assistant personalities (e.g., tutor, friend, coder)
> * Deploy on Streamlit Cloud
> * Add usage analytics

> #### 🙌 Acknowledgements
>
> * [OpenAI](https://platform.openai.com/docs/)
> * [Streamlit](https://docs.streamlit.io/)

---

### 🧠 2. Object Detector using OpenCV and TensorFlow

> #### 📖 Project Description
>
> This project implements a **real-time object detection** system that uses **OpenCV** for video capture and rendering, combined with a **TensorFlow SSD MobileNet** model trained on the COCO dataset. It detects and localizes multiple objects in live webcam feeds, drawing bounding boxes and confidence scores.

> #### 🧰 Tech Stack / Tools Used
>
> * **Programming Language**: Python 3.x
> * **Libraries**: OpenCV, TensorFlow, NumPy
> * **Models**: SSD MobileNet V3 (COCO)
> * **IDE**: VS Code / Jupyter Notebook

> #### 🚀 Features
>
> * Live webcam feed object detection
> * Configurable detection threshold (`thresh`)
> * Bounding boxes with class labels and confidence scores
> * Robust file checks and graceful error handling
> * Press 'q' to quit and clean resource release

> #### 🗂️ File Structure
>
> ```
> object_detector/
> │
> ├── Object_Detector.py   # Main detection script
> ├── coco.names           # Class labels file
> ├── frozen_inference_graph.pb  # Pre-trained weights
> ├── ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt  # Model config
> ```

> #### ⚙️ How to Run
>
> 1. Navigate to the project directory:
>
>    ```bash
>    cd ML_Projects/object_detector
>    ```
> 2. Ensure all model files are present (`coco.names`, `.pb`, `.pbtxt`).
> 3. Install dependencies:
>
>    ```bash
>    pip install opencv-python tensorflow numpy
>    ```
> 4. Run the detector script:
>
>    ```bash
>    python Object_Detector.py
>    ```

> #### 📌 Future Improvements
>
> * Support video file input and batch processing
> * Integration with TensorFlow Lite for mobile deployment
> * Add GUI for parameter adjustments
> * Logging detections to a CSV or database

> #### 🙌 Acknowledgements
>
> * [OpenCV](https://opencv.org/)
> * [TensorFlow](https://www.tensorflow.org/)
> * COCO Dataset contributors
