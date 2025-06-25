# 🧠 PDF Summarization using LangChain + OpenAI

This repository contains two versions of a PDF summarizer implemented in Jupyter notebooks using **LangChain**, **OpenAI GPT-3.5**, and **Python**. The summarizers take input from a PDF file and generate concise summaries.

---

## 📁 Contents

- `summarizer.ipynb` – Uses **chunking** to break the PDF into smaller parts before summarization.
- `updated summarizer.ipynb` – Uses **non-chunked**, page-specific summarization with selected improvements.

---

## 🆚 Key Differences

| Feature                      | `summarizer.ipynb` (Original)               | `updated summarizer.ipynb` (Updated)             |
|------------------------------|---------------------------------------------|--------------------------------------------------|
| **Text Chunking**            | ✅ Yes – Uses `RecursiveCharacterTextSplitter` | ❌ No – Summarizes full text from selected pages |
| **PDF Library**              | `PyPDF2`                                     | `PyMuPDF` (`fitz`) for more accurate extraction  |
| **Page Selection**           | Entire PDF                                  | Specific pages (e.g., 3–5)                       |
| **LLM Call**                 | Summarizes each chunk separately             | Summarizes full text in one go                   |
| **API Key Handling**         | Uses a Python `env.py` file                  | Loads from `.env.txt` using `python-dotenv`      |

---

## 📚 How the Summarizers Work

### 🔹 `summarizer.ipynb` – With Chunking
1. Extracts full text from the PDF using `PyPDF2`.
2. Splits the text into overlapping chunks (1000 characters with 100 overlap).
3. Summarizes each chunk using GPT-3.5 via LangChain.
4. Combines all chunk summaries into a final summary.

> Useful for summarizing large documents while avoiding token limit issues.

---

### 🔹 `updated summarizer.ipynb` – Without Chunking
1. Extracts text **only from selected pages** using `PyMuPDF (fitz)`.
2. Combines all selected text into one block.
3. Sends the entire text block to GPT-3.5 with a customizable instruction prompt.
4. Prints the full summary in one go.

> Best suited for smaller documents or when summarizing specific pages.


