# ⚡ SpekForge Pro

An enterprise-grade content migration, library auditing, and structural optimization engine built explicitly for modern revenue enablement teams. 

🔗 **Live Production Application:** [https://spekforge-pro.streamlit.app/](https://spekforge-pro.streamlit.app/)

## 🚀 The Core Challenge Solved
In the enterprise enablement space, migrating legacy content into short, structured knowledge systems usually means dealing with thousands of pages of text packed with **AI slop**, corporate fluff, and passive machine chatter. This tool automates that migration workflow by analyzing text health, auditing duplicate/obsolete setups, and refactoring content into highly scannable, human-grade operational copy.

## 🎛️ Architecture & Feature Matrix
* **Content Architecture (Forge):** Programmatically strips away corporate fluff and verbose transitions. Enforces a strict visual markdown hierarchy (**bolding**, callouts, bullet spacing) optimized for under-10-second consumption during live client calls.
* **Content Audit & Migration Strategy:** Evaluates content redundancy, text density, and provides strict migration recommendations (`KEEP`, `REWRITE`, `RETIRE`) along with an immediate action plan.
* **Dual Ingestion Engine:** Supports native unstructured text pasting alongside an automated local parsing system for raw `PDF` and `TXT` customer file uploads.

## 🛠️ Tech Stack
* **Frontend UI:** Streamlit (Custom CSS & Premium HTML Infusions)
* **LLM Orchestration:** Groq SDK (Powered by `llama-3.3-70b-versatile` & `mixtral-8x7b-32768` architectures)
* **Document Processing:** PyPDF Pipeline Engine
