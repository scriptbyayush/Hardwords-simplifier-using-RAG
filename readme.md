
# Complex Word Identification and Text Simplification using RAG

## Overview

This project implements a Retrieval-Augmented Generation (RAG) based system for **Complex Word Identification (CWI)** and **Text Simplification** in Hindi and Marathi. The system identifies complex words in a sentence and replaces them with simpler alternatives using a knowledge base and a locally hosted Large Language Model (LLaMA 3 via Ollama).

The project also includes an evaluation framework to measure simplification accuracy.

---

## Features

- Complex Word Identification (CWI)
- Rule-based and dictionary-based simplification
- Retrieval-Augmented Generation (RAG) pipeline
- Local LLM integration using Ollama (no API cost)
- Evaluation metrics (accuracy, word-level analysis)
- Streamlit-based user interface

---

## Project Structure

```
rag_simplifier/
│
├── app.py          # Streamlit UI
├── main.py         # Pipeline controller
├── cwi.py          # Complex word detection
├── retriever.py    # Retrieval logic (RAG)
├── generator.py    # LLM interaction
├── utils.py        # Helper functions
├── data/
│   └── knowledge.json  # Word mappings
└── requirements.txt    # Dependencies
```

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/scriptbyayush/Hardwords-simplifier-using-RAG
cd Hardwords-simplifier-using-RAG
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not configured, install manually:
```bash
pip install sentence-transformers faiss-cpu streamlit transformers torch
```

### 3. Install Ollama

Download and install Ollama from: [https://ollama.com](https://ollama.com/)

After installation, restart your terminal.

### 4. Download and Run LLaMA 3 Model

```bash
ollama run llama3
```

This command will:
- Download the model (first time only)
- Run it locally (offline usage supported after download)

## Running the Application

**Step 1:** Start the Streamlit App
```bash
streamlit run app.py
```

**Step 2:** Run LLaMA 3 (if not already running)
```bash
ollama run llama3
```

## Sample Input/Output

**Input:**  
`सामाजिक अंकेक्षण में ग्रामीणों की भागीदारी अत्यंत महत्त्वपूर्ण है`

**Output:**
- Simplified sentence
- Identified complex words
- Word-level simplifications
- Evaluation metrics (optional)

---

## Evaluation

The system evaluates performance based on:
- Total number of words
- Number of complex words
- Number of simplified words
- Simplification accuracy (%)

**Accuracy Formula:**  
\[ \text{Accuracy} = \left( \frac{\text{Simplified Words}}{\text{Total Complex Words}} \right) \times 100 \]

Current system achieves **over 96% accuracy** on Hindi and Marathi dataset.

## Dataset

- 100 Hindi sentences
- 100 Marathi sentences
- Formal domain: government notices, policies, administrative text

Each sentence includes:
- Identified complex words
- Simplified outputs
- Evaluation score

## GitHub Repository

**Source Code:**  
[https://github.com/scriptbyayush/Hardwords-simplifier-using-RAG](https://github.com/scriptbyayush/Hardwords-simplifier-using-RAG)

## Notes

- Runs **completely offline** after model download
- **No paid APIs** required
- Performance depends on dictionary coverage and prompt design

## Author

**Ayush Vaidya**

















##


##


##
