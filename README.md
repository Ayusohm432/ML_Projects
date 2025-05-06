---
## 💡 **ML_Projects**

This repository contains a curated collection of machine learning and AI-based mini-projects built using Python. Each project focuses on solving real-world problems using modern tools, libraries, and frameworks. The goal is to explore end-to-end ML and AI workflows—from data preparation to deployment-ready applications.

---

## ✅ **README for ML Projects**

## 📚 List of Projects

1. **[GPT-3.5 ChatBot using Streamlit](#1-gpt-35-chatbot-using-streamlit)**  
   An interactive AI-powered chatbot app that leverages OpenAI's GPT-3.5 model with a Streamlit UI.

*(More projects will be added soon...)*

---

## 🧠 1. GPT-3.5 ChatBot using Streamlit

### 📖 Project Description

This project implements an AI chatbot using **OpenAI's GPT-3.5 model** within a **Streamlit** web interface. It handles real-time user queries, maintains session-based chat history, and responds conversationally. The app is lightweight and well-suited for experimenting with LLM integration.

---

### 🧰 Tech Stack / Tools Used

* **Programming Language**: Python 3.x  
* **Libraries**: Streamlit, OpenAI, JSON, OS  
* **IDE**: VS Code / Jupyter Notebook  
* **API**: OpenAI GPT-3.5-turbo  
* **Deployment**: Localhost or Streamlit Cloud

---

### 🚀 Features

* Responsive chatbot interface
* Persistent chat memory with Streamlit session state
* API key securely read from a `config.json` file
* GPT-3.5-turbo integration via `openai.ChatCompletion`
* Simple and elegant user interface using Streamlit

---

### 🗂️ File Structure

```

chatbot/
│
├── app.py               # Streamlit app
├── config.json          # Contains API key (excluded from version control)

````

---

### ⚙️ How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/Ayusohm432/ML_Projects.git
   cd ML_Projects/chatbot
````

2. Create `config.json` with your OpenAI API key:

   ```json
   {
     "OPENAI_API_KEY": "your-api-key-here"
   }
   ```

3. Install dependencies:

   ```bash
   pip install streamlit openai
   ```

4. Launch the app:

   ```bash
   streamlit run app.py
   ```

---

### 📌 Future Improvements

* Add voice input/output
* Add multiple assistant personalities (e.g., tutor, friend, coder)
* Deploy on Streamlit Cloud
* Add usage analytics

---

### 🙌 Acknowledgements

* [OpenAI](https://platform.openai.com/docs/)
* [Streamlit](https://docs.streamlit.io/)

---