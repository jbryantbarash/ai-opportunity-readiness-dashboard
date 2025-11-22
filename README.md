# AI Opportunity & Change Readiness Evaluator

An interactive Streamlit dashboard for **prioritizing AI and automation use cases** based on business value, technical feasibility, data readiness, change impact, and risk.

This project demonstrates how an **AI Consultant / AI Transformation Lead** evaluates, scores, and communicates which AI initiatives an organization should pursue first — aligning directly with enterprise AI strategy, proof-of-concept selection, change management, and value realization.

---

## 🚀 Why This Project Exists

Organizations across industries have no shortage of AI ideas — but they often lack a **clear, structured, and repeatable method** to:

- Identify high-value AI opportunities  
- Evaluate technical feasibility and data readiness  
- Assess organizational change impact  
- Reduce risk during early exploration  
- Build prioritization frameworks executives can trust  
- Align cross-functional teams around a unified roadmap  

This tool solves that problem.

It enables business leaders, data teams, and consultants to **co-create an AI opportunity portfolio**, using transparent scoring, adjustable weighting, and intuitive visualizations to identify quick wins and high-value strategic investments.

---

## ✨ Key Features

### 🧮 Dynamic Scoring Model
Each opportunity is scored on:

- **Business Value (1–5)**
- **Technical Feasibility (1–5)**
- **Data Readiness (1–5)**
- **Change Impact (1–5)** *(penalty → higher impact reduces priority)*
- **Risk (1–5)** *(penalty → higher risk reduces priority)*

All weights are adjustable in real time via the sidebar, allowing teams to explore different strategies such as value-first, feasibility-first, low-risk-first, or rapid experimentation.

---

### 📊 Interactive Visualizations

#### **1. Ranked Opportunity List**
A sortable bar chart showing each use case ordered by **Priority Score**.

#### **2. Value vs. Feasibility Matrix**
A 2×2 bubble plot showing:

- High-value quick wins  
- Long-term strategic bets  
- High-impact, high-risk opportunities  

Bubble size = Priority Score  
Bubble color = Readiness Score

---

### 📋 Collaborative Use Case Table

- Add, edit, or delete opportunities directly in the interface  
- Update scoring values in real time  
- Perfect for **workshops with business partners**  
- Helps drive alignment during discovery phases  

---

### 📝 Executive-Ready Narrative Summary

A narrative panel automatically explains:

- Top-ranked opportunities  
- Why they are high-priority  
- Where to begin POCs  
- Strategic considerations  
- Organizational readiness indicators  

This is particularly useful for leadership sessions and portfolio reviews.

---

## 🧠 How This Demonstrates AI Consulting Skills

This repository showcases real-world AI consulting competencies, including:

- **AI opportunity assessment & portfolio creation**  
- Structured **feasibility and readiness evaluation**  
- Clear executive communication & storytelling  
- Cross-functional alignment (Business, IT, Data, Change)  
- Prioritization frameworks grounded in value and risk  
- Early-stage POC scoping and roadmap creation  
- Experience balancing **people, process, technology**  
- Change-management thinking in an AI transformation context  

This directly aligns with roles in:

- AI Strategy  
- AI Consulting  
- Enterprise AI Transformation  
- Digital Transformation  
- AI Product Leadership  
- Change Management for AI  
- Operations & Process Automation  

---

## 🛠️ Tech Stack

- **Streamlit** — for interactive UI  
- **Pandas** — scoring logic & data manipulation  
- **Plotly** — dynamic visualizations  
- **Python 3.9+**  
- **CSV data layer** — simple, transparent, workshop-friendly  

---

## 📁 Project Structure

ai-opportunity-readiness-dashboard/
│
├── app.py # Main Streamlit app
├── requirements.txt # Dependencies
├── sample_use_cases.csv # Example use-case dataset
└── README.md # Project documentation


---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone git@github.com:jbryantbarash/ai-opportunity-readiness-dashboard.git
cd ai-opportunity-readiness-dashboard
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run app.py
```

Your browser will open to:

http://localhost:8501

<img width="1383" height="695" alt="Screenshot 2025-11-22 at 3 25 58 PM" src="https://github.com/user-attachments/assets/28837ad3-4c86-4ad2-a2fa-af1e877db159" />



