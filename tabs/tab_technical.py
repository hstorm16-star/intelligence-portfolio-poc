"""
tabs/tab_technical.py
Technical tooling, chain coverage, and certifications tab.
"""

import streamlit as st


TOOLS = [
    ("Chainalysis Reactor / KYT",
     "Core platform — entity attribution, sanctions screening, alert triage, clustering, KYT transaction monitoring",
     95),
    ("TRM Labs (ACE + CI)",
     "Cross-chain tracing, risk scoring, typology research, threat actor and sanctions data",
     85),
    ("Elliptic",
     "Holistic screening, DeFi exposure analysis, multi-asset tracing",
     72),
    ("Flashpoint",
     "Threat actor forum intelligence, open-source enrichment, dark web signals",
     60),
    ("Python / SQL",
     "Data analysis, investigative workflow support, large dataset querying and manipulation",
     68),
    ("OSINT workflows",
     "Infrastructure mapping, entity verification, forum monitoring, open-source signal fusion",
     88),
]

CHAINS = [
    ("Bitcoin (BTC)",          "#F7931A"),
    ("Ethereum (ETH)",         "#627EEA"),
    ("Solana (SOL)",           "#9945FF"),
    ("TRON (TRX)",             "#EF0027"),
    ("DeFi / bridge flows",    "#1D9E75"),
    ("Multi-chain ecosystems", "#888780"),
]

CERTS = [
    ("ACAMS CCAS",
     "Certified Crypto Asset Specialist — Association of Certified Anti-Money Laundering Specialists"),
    ("Chainalysis CISC + Reactor / KYT",
     "Certified Investigator — platform specialist across Reactor and KYT tooling"),
    ("TRM ACE + CI track",
     "Advanced Certified Expert + Crypto Investigations track — cross-chain tracing and typology specialisation"),
]


def render() -> None:
    st.markdown("### Analytical tooling")
    for name, desc, depth in TOOLS:
        st.markdown(
            f"""
            <div class="tool-row">
              <div class="tool-name">{name}</div>
              <div class="tool-desc">{desc}</div>
              <div class="tool-bar">
                <div class="tool-fill" style="width:{depth}%"></div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown("### Blockchain & ecosystem coverage")
    pills_html = "".join(
        f'<span style="display:inline-flex;align-items:center;gap:6px;padding:5px 11px;'
        f'border-radius:20px;font-size:12px;margin:3px;border:1px solid #e8e8e8;background:#fff">'
        f'<span style="width:8px;height:8px;border-radius:50%;background:{color}"></span>{label}</span>'
        for label, color in CHAINS
    )
    st.markdown(
        f'<div style="display:flex;flex-wrap:wrap;gap:2px;margin-bottom:1rem">{pills_html}</div>',
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.markdown("### Certifications")
    for cert, desc in CERTS:
        st.markdown(
            f"""
            <div style="padding:10px 0;border-bottom:1px solid #f0f0f0">
              <div style="font-size:13px;font-weight:600;margin-bottom:3px">{cert}</div>
              <div style="font-size:12px;color:#666">{desc}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
