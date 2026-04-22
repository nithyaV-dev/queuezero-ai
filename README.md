# 🚀 QueueZero AI – Smart Healthcare Queue Agent

## 🧠 Problem
Hospital queues are inefficient. Patients don’t know:
- Which department is less crowded
- When to visit
- How long they will wait

This leads to:
❌ Long waiting times  
❌ Overcrowding  
❌ Poor patient experience  

---

## 💡 Solution
QueueZero AI is an **Autonomous AI Agent** that:

- Reads live queue data from Google Sheets
- Analyzes multiple booking slots
- Rejects bad options
- Selects the best slot using reasoning
- Automatically books token
- Handles emergency priority cases

---

## ⚙️ Features

### 🤖 AI Slot Optimization
- Evaluates multiple slots
- Considers:
  - Waiting time
  - Crowd level
  - Tokens left
- Performs **self-correction**

---

### 🧠 AI Reasoning
Example:
Slot 1 rejected → high wait ⚠️
Slot 2 rejected → no tokens ❌
Slot 3 selected → optimal ✅


---

### 📊 Real-Time Data
- Connected with Google Sheets API
- Live token updates

---

### 🚨 Emergency Mode
- Instantly assigns **Token 1**
- Bypasses normal logic
- Shows priority reasoning

---

### 🎬 Animated AI Flow
Simulates real AI thinking:

- 🔍 Reading live data  
- 📊 Detecting patterns  
- 🧠 Comparing slots  
- ⚡ Booking token  

---

## 🛠 Tech Stack

- Python
- Streamlit (UI)
- Google Sheets API
- gspread
- OAuth2

---

## 📂 Project Structure
queuezero-ai/
│── app.py
│── api.py
│── agent.py
│── gsheet.py
│── credentials.json
│── requirements.txt
│── README.md


---

## ▶️ How to Run

IN POWERSHELL TERMINAL:-
RUN BELOW THESE
pip install -r requirements.txt
streamlit run app.py

---
🎯 Innovation
This is not a normal app.
👉 It behaves like an AI agent
👉 Makes decisions, not just UI actions
👉 Shows reasoning + self-correction
---
🚀 Future Scope
->Real hospital integration
-->Mobile app
-->Predictive rush analysis
-->Voice assistant
---
## 👤Author
**Nithya Vasireddi**  
AI Enthusiast | Developer  
Built for **AI Agentathon 🚀**
---