# Data-Science-Internship-Assessment
# 📄 GenAI Document Assistant

A full-stack GenAI-powered assistant that understands documents — upload any PDF or TXT file, and the system can:

- 📝 Summarize the content  
- ❓ Answer your questions  
- 🚀 Automatically generate practice questions  
- 📊 Evaluate your answer and provide intelligent feedback

Built using **LangChain**, **Flan-T5**, **Django**, and **Streamlit**.

---

## 🧠 Features

| Feature | Description |
|--------|-------------|
| 📤 Upload Document | Upload `.pdf` or `.txt` files |
| 📝 Summary | Generate a short, meaningful summary |
| ❓ Ask a Question | Ask anything from the document |
| 🚀 Challenge Mode | Auto-generate 1 question for once |
| 📊 Feedback | Submit answers and get performance feedback |

---

## 🛠 Tech Stack

| Layer | Tools |
|------|-------|
| ⚙️ Backend | Django, DRF, LangChain, HuggingFace Transformers |
| 🧠 LLM | Flan-T5 (text2text-generation) |
| 🔍 Search | FAISS vector store + semantic embeddings |
| 📤 Frontend | Streamlit |
| 📚 NLP Utils | PyMuPDF for PDFs, sentence-transformers |

---

## 📦 Project Structure
- genai_project/
-  |—assistant/
-   |  ├── views.py
-   |  ├── urls.py
-   |  ├── models.py
-   |  └── ...
-   ├── backend/ # LangChain logic
-   \_│ ├── challenge.py
-   │ ├── qa_engine.py # Core NLP + question logic
-   │ └── ...
-   ├── genai_project/
-   | ├── setting.py
-   | ├── urls.py
-   | ├── app.py
-   | └── ...
- │ app.py # Streamlit UI
- ├── temp/ # Uploaded files (optional)
- ├── requirements.txt
- ├── README.md


---

## 🚀 How to Run

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/genai-doc-assistant.git
cd genai-doc-assistant
```
### 2. Create Virtual Environment and Install requirements
```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
### 3.Run Django Backend
```bash
cd genai_project
py manage.py run server
```

### 4. Run streamlit 
Open Another terminal where app.py available
### Run this Command
```bash
streamlit run app.py
```

# End
