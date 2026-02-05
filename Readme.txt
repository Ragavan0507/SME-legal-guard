# ⚖️ SME Legal Guard
### *AI-Powered Risk Auditor & Negotiation Assistant for Indian SMEs*

**SME Legal Guard** is a "Legal-Tech" solution designed to empower small and medium-sized business owners. It simplifies complex legal jargon, identifies hidden risks in contracts, and provides actionable negotiation strategies in both **English and Hindi**.

---

## 🌟 Features

- **📄 Multi-Format Support:** Instantly analyze **PDF, DOCX, and TXT** contracts.
- **🚩 Intelligent Risk Audit:** Get a **1-100 Risk Score** and a breakdown of High, Medium, and Low-risk clauses.
- **🇮🇳 Bilingual Clarity:** Clause-by-clause explanations in **English** and **Hindi** to ensure no business owner is left behind.
- **💡 Negotiation Alternatives:** For every risk found, the AI suggests **specific wording or counter-proposals** to use with the other party.
- **📁 Pro-SME Templates:** A built-in hub for downloading safe, industry-standard **NDA, Service, and Employment templates**.
- **📥 PDF Export:** Generate and download professional **Risk Audit Reports** to share with your team or legal advisor.
- **📋 Session Audit Trail:** Keep track of all documents analyzed during your current session.

---

## 🛠️ Tech Stack

- **Core Engine:** [Python 3.9+](https://www.python.org/)
- **Frontend/UI:** [Streamlit](https://streamlit.io/)
- **AI Model:** GPT-4o-mini (via GitHub Models API)
- **Document Processing:** - `pdfplumber` (PDF Extraction)
  - `python-docx` (Word Extraction)
- **Report Generation:** `FPDF`

---

## 🚀 Getting Started

### 1. Installation
Clone the repository and install the required dependencies:
```bash
git clone [https://github.com/YOUR_USERNAME/sme-legal-guard.git](https://github.com/YOUR_USERNAME/sme-legal-guard.git)
cd sme-legal-guard
python -m pip install -r requirements.txt