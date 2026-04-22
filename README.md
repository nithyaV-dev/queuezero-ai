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

## 📁 Project Structure

• app.py — Streamlit UI (Frontend)  
• api.py — API layer (handles requests)  
• agent.py — AI decision engine (logic + reasoning)  
• gsheet.py — Google Sheets integration  

• requirements.txt — Python dependencies  
• README.md — Project documentation  
• .gitignore — Ignored files  

---

## ▶️ How to Run

- Open PowerShell / Terminal  
- Install dependencies:
  - `pip install -r requirements.txt`
- Run the app:
  - `streamlit run app.py`
- Open browser:
  - `http://localhost:8501`

---
## 🎯 Innovation

- This is not a normal app — it behaves like an AI agent  
- Makes autonomous decisions, not just UI actions  
- Performs real-time slot analysis  
- Compares multiple options before selecting  
- Shows transparent AI reasoning  
- Includes self-correction (rejects bad slots → selects optimal one)  
- Simulates real-world hospital queue intelligence  
---
## 🚀 Future Scope

- Real hospital system integration  
- Mobile application version  
- Predictive rush analysis using historical data  
- Voice assistant for patient interaction  
- Multi-hospital scaling with live dashboards  
---
## 👤 Author

**Nithya Vasireddi**  
AI Enthusiast • Developer  
🔗 GitHub: https://github.com/nithyav-dev  
🚀 Built for AI Agent Hackathon
---
