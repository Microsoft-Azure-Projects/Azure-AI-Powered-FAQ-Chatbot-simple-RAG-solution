# Azure-AI-Powered-FAQ-Chatbot
# 🤖 AI-powered FAQ Chatbot (Azure Cognitive Search + Azure Bot Service + OpenAI)

## 📌 Project Overview
This project demonstrates how to build an **AI-powered FAQ chatbot** that can automatically answer customer queries using a **knowledge base (FAQs)**, provide a **conversational interface** with Azure Bot Service, and enhance responses with **Azure OpenAI** for more natural dialogue.  

👉 **Use Case:** Customer support automation  

---

## 🏗️ Architecture

1. User asks a question in the chatbot interface  
2. **Azure Bot Service** receives the query  
3. Query is passed to **Azure Cognitive Search (FAQ Knowledge Base)**  
4. Best-matched FAQ answer is retrieved  
5. Answer is refined with **Azure OpenAI (GPT-35/4)** into natural language  
6. Bot replies back to the user

   flowchart LR
   
    A[faq.csv (Knowledge Base)] --> B[Azure Cognitive Search (FAQ Index)]
   
    B --> C[search_faq() in Streamlit]
   
    C --> D[Azure OpenAI (Refine Response)]
   
    D --> E[Streamlit UI: Display Answer]
   

---

## 🔧 Azure Services Used
- **Azure Cognitive Search** – stores and retrieves FAQ data  
- **Azure Bot Service** – provides chatbot interface  
- **Azure OpenAI Service** – refines answers into conversational responses  
- **(Optional)** Azure App Service / Channels (Teams, Slack, Web Chat) for deployment  

---
## Project Structure

AI-FAQ-Chatbot/

│── app.py

│── azure_config.py

│── requirements.txt

│── services/

│   ├── cognitive_search.py

│   ├── openai_chat.py

│   └── bot_connector.py   # optional

│── data/

│   └── FAQ.csv            # Knowledge base (questions + answers)

│── README.md

│  --- screenshots
          











