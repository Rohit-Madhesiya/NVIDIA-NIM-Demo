---
title: NVIDIA NIM Demo
emoji: 🔥
colorFrom: purple
colorTo: yellow
sdk: streamlit
sdk_version: 1.42.2
app_file: app.py
pinned: false
license: apache-2.0
short_description: 'AI-powered document retrieval and question-answering system '
---

# NVIDIA DeepSeek AI Document Search

## Overview 🧠📄
This project is an AI-powered **document retrieval and question-answering system** utilizing **NVIDIA DeepSeek AI** and **FAISS vector stores**. It allows users to **embed, retrieve, and query research papers** using advanced **NVIDIA AI models** for accurate and contextual responses.

## Features ✨
- **FAISS-based Vector Storage:** Efficiently stores and retrieves document embeddings.
- **NVIDIA DeepSeek AI Integration:** Uses **deepseek-ai/deepseek-r1** for high-quality AI inference.
- **PDF Processing:** Extracts and processes research papers for retrieval-based QA.
- **Streamlit UI:** Interactive user interface for querying and document similarity search.

## Deployment 🚀
The application is deployed on **Hugging Face Spaces**. You can access it using the following link:

👉 **[Deployment Link](https://huggingface.co/spaces/guptarohit20/NVIDIA-NIM-Demo)** 

## Installation & Setup 🛠️
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Rohit-Madhesiya/NVIDIA-NIM-Demo.git
cd NVIDIA-NIM-Demo
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up API Key
- Create a `.env` file in the root directory.
- Add the following line:
```env
NVIDIA_API_KEY=<your_nvidia_api_key>
```

## Usage 📌
Run the Streamlit application:
```bash
streamlit run main.py
```

Once the app is running:
1. Enter your **NVIDIA API Key**.
2. Click **Document Embedding** to process research papers.
3. Type a **question** and get AI-generated responses based on the document content.
4. Expand **Document Similarity Search** to view retrieved document chunks.

## Dependencies 📋
The project requires the following Python libraries:
- `streamlit`
- `langchain_nvidia_ai_endpoints`
- `langchain_community`
- `faiss-cpu`
- `pypdf`
- `python-dotenv`
- `openai`

## Project Structure 📂
```
├── main.py              # Main application file
├── requirements.txt     # List of dependencies
├── .env                 # API key configuration (not included in repo)
└── README.md            # Project documentation
```

## Contributing 🤝
Feel free to fork the repository, submit pull requests, or report any issues.

## Author 👨‍💻
Developed by **[Rohit Gupta]**.

