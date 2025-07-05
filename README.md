# 📚 Relevance-Based Research Paper Recommender

## 🧠 Overview

The **Relevance-Based Research Paper Recommender** is a full-stack web application that helps users quickly discover the most **semantically relevant research papers** on arXiv based on a user’s topic of interest.

It utilizes **Natural Language Processing** techniques to go beyond simple keyword matching — by computing **semantic similarity** between the user's query and paper abstracts using **SentenceTransformers**.

---

## ❓ Problem Solved

In academic and research domains, sifting through thousands of papers to find the most relevant ones is time-consuming.

This project solves that by:

✅ Replacing keyword-based search with **semantic understanding**.  
🔍 Accurately identifying **contextually relevant** research papers.  
⚡ Improving **search efficiency** and **user productivity**.  

**Use Case:**  
Ideal for students, researchers, and professionals who want faster access to high-quality academic content in AI, ML, and NLP.

---

## ✨ Features

🧠 **Semantic Matching:** Uses SentenceTransformers to compare user queries with paper abstracts.  
🔎 **Live Search Interface:** Search papers in categories like cs.AI, cs.CL, cs.LG.  
⚙️ **Flask Backend:** Processes queries, fetches data from arXiv API, ranks results.  
🖥️ **Interactive UI:** Clean frontend displays title, score, summary snippet, and a link.  
📈 **Relevance Bar:** Visual indicator showing match percentage.  
🗂️ **Modal Popup:** Click a paper card to view complete details in a modal.  

---

## 🧑‍💻 Tech Stack

### 🔹 Frontend
- HTML
- CSS
- JavaScript  
- Responsive Design with Flexbox

### 🔹 Backend
- Python (Flask)
- SentenceTransformers (`all-MiniLM-L6-v2`)
- arXiv API (`arxiv` Python package)
- Requests, JSON handling

---
<img width="1440" alt="RPR1" src="https://github.com/user-attachments/assets/fabcdff6-860f-4caf-96fa-19c46d15d60e" />

<img width="1440" alt="RPR2" src="https://github.com/user-attachments/assets/063461dd-3ca2-45fe-a194-ed0cced559b1" />

---
## 🚀 How It Works

1. 📝 User enters a topic (e.g., *machine learning*)  
2. 📬 Flask backend sends a query to arXiv API  
3. 📄 Fetches abstracts, computes semantic similarity with SentenceTransformer  
4. 🔢 Results are ranked by relevance score  
5. 🧾 Displays paper cards with brief preview, authors, and modal popup  
6. 🔗 Click to view the full paper on arXiv.org

---
