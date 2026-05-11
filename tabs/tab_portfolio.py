"""
tabs/tab_portfolio.py
Portfolio framing and anonymisation guidance tab.
"""

import streamlit as st


NARRATIVES = [
    {
        "color": "#185FA5",
        "role": "Sanctions nexus & adversarial financial ecosystem analysis",
        "text": (
            "Specialised in OFAC SDN exposure analysis, cross-chain sanctions evasion investigation, "
            "and state-linked financial ecosystem analysis — covering Iranian oil procurement flows and "
            "VASP wallet rotation, Russian Garantex-adjacent networks and high-risk RUB payment "
            "infrastructure (Heleket, Cryptomus), and DPRK-linked IT worker ecosystem activity. "
            "Handled highest-sensitivity APAC escalations. Compliance Star Award recipient."
        ),
    },
    {
        "color": "#993C1D",
        "role": "Counter-threat finance & national-security-adjacent workstreams",
        "text": (
            "Contributed to counter-threat finance investigations involving DPRK-linked actors, "
            "extremist financing networks, and national-security-adjacent financial infrastructure — "
            "applying cross-chain adversarial tracing and entity attribution methodology under "
            "high-sensitivity reporting conditions. Analytical standards informed by prior law "
            "enforcement investigative experience at NZ Police."
        ),
    },
    {
        "color": "#854F0B",
        "role": "Intelligence fusion methodology & internal enablement",
        "text": (
            "Led intelligence fusion across OSINT, on-chain analytics, vendor threat intelligence, "
            "and operational inputs — enabling proactive detection ahead of platform impact. Delivered "
            "large-scale internal briefing on Huione/Xinbi/guarantee system infrastructure. Led "
            "internal intelligence fusion training. Developed investigative frameworks and typology "
            "playbooks standardising high-complexity case handling."
        ),
    },
    {
        "color": "#3B6D11",
        "role": "LE-grade intelligence production & strategic reporting",
        "text": (
            "Produced intelligence packages supporting VARA regulatory reporting and LE-aligned "
            "dissemination pathways. Evidential standards shaped by prior specialist investigator "
            "experience at NZ Police Virtual Assets Unit — criminal and civil proceedings, "
            "post-seizure asset recovery (12k USD, Solana). Outputs designed to withstand legal "
            "and regulatory challenge."
        ),
    },
    {
        "color": "#534AB7",
        "role": "Technical depth & multi-jurisdiction ecosystem coverage",
        "text": (
            "Investigated across BTC, ETH, SOL, TRON, and DeFi/bridge ecosystems. Core tooling: "
            "Chainalysis Reactor/KYT, TRM Labs (ACE + CI), Elliptic, Flashpoint, Python/SQL, OSINT "
            "workflows. Certified: ACAMS CCAS, Chainalysis CISC, TRM ACE + CI. Jurisdictional scope: "
            "Iran, Russia, DPRK, Southeast Asia, Western cybercrime infrastructure, dual-use "
            "procurement networks."
        ),
    },
]

ANON_NO = [
    "Case reference IDs — describe as 'a sanctions nexus investigation' not a specific reference",
    "Active counterparty or VASP names from live investigations — use 'a high-risk payment provider' or 'a nested exchange network'",
    "Wallet addresses and transaction hashes — describe flows by typology and methodology",
    "Specific LE dissemination targets — use 'LE-aligned intelligence pathways' or 'regulatory dissemination support'",
    "Customer UIDs or account identifiers — reference 'account-level risk assessment' generically",
]

ANON_OK = [
    "Publicly reported ecosystems (Garantex, Huione, Xinbi, Scattered Spider, Heleket/Cryptomus as named entities in public reporting)",
    "Investigative methodology, tooling, certifications, career milestones",
    "Aggregate outcomes and strategic impact descriptions",
]


def render() -> None:
    st.markdown("### Interview-ready framing")

    for n in NARRATIVES:
        st.markdown(
            f"""
            <div class="ps-block" style="border-left-color:{n['color']}">
              <div class="ps-role" style="color:{n['color']}">{n['role']}</div>
              <div class="ps-text">{n['text']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown("### Anonymisation guidance")

    st.markdown("**Do not disclose in interviews:**")
    for item in ANON_NO:
        st.markdown(f'<div class="anon-no">✗ &nbsp;{item}</div>', unsafe_allow_html=True)

    st.markdown("<br>**Safe to reference:**", unsafe_allow_html=True)
    for item in ANON_OK:
        st.markdown(f'<div class="anon-ok">✓ &nbsp;{item}</div>', unsafe_allow_html=True)
