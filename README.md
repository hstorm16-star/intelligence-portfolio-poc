# Intelligence Portfolio — Threat Finance & Sanctions Investigations

**Proof-of-concept portfolio dashboard.**  
All data is sanitised. No confidential, sensitive, or internal operational information is disclosed.

---

## Overview

A Streamlit-based career and capability portfolio for a senior intelligence analyst
specialising in sanctions nexus investigations, counter-threat finance, adversarial financial
network analysis, and blockchain intelligence fusion.

---

## Project structure

```
intel_portfolio/
├── app.py                   # Main Streamlit entry point
├── requirements.txt         # Pinned Python dependencies
├── runtime.txt              # Python version for Streamlit Cloud
├── README.md                # This file
│
├── data/                    # Sanitised JSON data files
│   ├── workstreams.json
│   ├── ecosystems.json
│   ├── investigations.json
│   ├── methodologies.json
│   └── impact.json
│
├── tabs/                    # One module per dashboard tab
│   ├── __init__.py
│   ├── tab_overview.py
│   ├── tab_ecosystems.py
│   ├── tab_investigations.py
│   ├── tab_methodology.py
│   ├── tab_technical.py
│   ├── tab_background.py
│   ├── tab_impact.py
│   └── tab_portfolio.py
│
└── utils/                   # Shared utilities
    ├── __init__.py
    ├── data_loader.py       # JSON loader with st.cache_data
    └── styles.py            # Global CSS injection
```

---

## Running locally

```bash
# 1. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python3 -m streamlit run app.py
```

The app will open at `http://localhost:8501`.

---


---

## Tabs

| Tab | Content |
|-----|---------|
| Overview | Investigative workstreams and domain summary |
| Threat ecosystems | Adversarial financial ecosystems investigated |
| Representative work | Anonymised operational investigation summaries |
| Methodology | Intelligence fusion workflow and investigative methodologies |
| Technical | Tooling, chain coverage, certifications |
| Background | Career timeline and operational contributions |
| Strategic impact | Evidence of impact and industry engagement |
| Portfolio framing | Interview-ready narrative blocks and anonymisation guide |

---

## Important notes

- This is a **proof-of-concept portfolio dashboard** only.
- No confidential case data, wallet addresses, transaction hashes, customer identifiers,
  or sensitive counterparty information is included anywhere in this project.
- Ecosystem names referenced (Garantex, Huione, Xinbi, Scattered Spider, Heleket, Cryptomus)
  are entities reported publicly in open-source intelligence and industry reporting.
- This project contains no secrets, API keys, or credentials of any kind.

---

