"""
tabs/tab_background.py
Career background and operational contributions tab.
"""

import streamlit as st


TIMELINE = [
    {
        "date": "Feb 2021 — Easy Crypto",
        "title": "Compliance manager & investigation lead",
        "detail": (
            "Promoted to compliance manager within 3 months, lead investigator within a year. "
            "Built AML/KYC operations from the ground up. Established operational relationships "
            "with NZ Police and exchange partners. Recognised by Chainalysis as a top community "
            "contributor. Trained frontline staff on AML/KYC and blockchain analytics tooling."
        ),
        "dot_color": "#bbb",
    },
    {
        "date": "Nov 2022 — Breadcrumbs.app",
        "title": "Blockchain intelligence analyst — data strategy",
        "detail": (
            "Led blockchain attribution data strategy — improving entity coverage and visibility "
            "at scale. Shaped product and research direction across technical and commercial client "
            "contexts. Produced client-facing intelligence outputs supporting investigative and "
            "compliance use cases."
        ),
        "dot_color": "#bbb",
    },
    {
        "date": "Jan 2024 — NZ Police (prior to Binance)",
        "title": "Specialist investigator — virtual assets unit",
        "detail": (
            "Specialist cryptocurrency tracing for asset recovery in criminal and civil proceedings. "
            "Operated to law enforcement evidential and procedural standards. Recovered 12k USD from "
            "a Solana staking account in a post-seizure investigation. This role directly informed "
            "the analytical rigour and reporting standards brought to subsequent commercial "
            "intelligence work."
        ),
        "dot_color": "#378ADD",
    },
    {
        "date": "May 2024 — Binance CIFC",
        "title": "Intelligence analyst → APAC escalation handling",
        "detail": (
            "Trusted with highest-sensitivity APAC escalations in the CIFC function. Led intelligence "
            "fusion methodology training. Delivered large-scale internal briefing on Huione, Xinbi, "
            "and guarantee system ecosystems. Compliance Star Award for sanctions nexus investigation "
            "quality. External speaker at TRM Customer Connect webinar, Jun 2025."
        ),
        "dot_color": "#378ADD",
    },
    {
        "date": "Apr 2026 — Binance CIFC",
        "title": "Interim operational support during team restructure",
        "detail": (
            "Took on broader coordination responsibilities during a period of team restructuring — "
            "escalation handling, investigative output coordination, and cross-functional intelligence "
            "support. Not a permanent managerial appointment."
        ),
        "dot_color": "#534AB7",
    },
]

CONTRIBUTIONS = [
    ("Large-scale internal intelligence briefing",
     "Team-wide presentation on Huione, Xinbi, guarantee systems, and Southeast Asian illicit "
     "payment infrastructure — elevating collective analytical awareness across the CIFC function."),
    ("Intelligence fusion training",
     "Internal training on combining OSINT, on-chain, and operational intelligence for proactive "
     "threat detection and higher-quality investigative output."),
    ("Investigative framework & typology development",
     "Standardised methodology for high-complexity case handling · documented typology patterns "
     "for sanctions, fraud, ML, and counter-threat finance workstreams."),
    ("Escalation coordination & cross-functional support",
     "Highest-sensitivity APAC referrals · coordination across compliance, legal, security, and "
     "risk · regulatory intelligence pathway support."),
]


def render() -> None:
    st.markdown("### Career background")

    for i, entry in enumerate(TIMELINE):
        is_last = i == len(TIMELINE) - 1
        line_html = (
            ""
            if is_last
            else f'<div class="tl-line"></div>'
        )
        st.markdown(
            f"""
            <div class="tl-wrap">
              <div class="tl-dot-col">
                <div class="tl-dot" style="background:{entry['dot_color']}"></div>
                {line_html}
              </div>
              <div class="tl-content">
                <div class="tl-date">{entry['date']}</div>
                <div class="tl-title">{entry['title']}</div>
                <div class="tl-detail">{entry['detail']}</div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown("### Operational contributions")

    for label, desc in CONTRIBUTIONS:
        st.markdown(
            f"""
            <div style="padding:10px 0;border-bottom:1px solid #f0f0f0">
              <div style="font-size:13px;font-weight:600;margin-bottom:3px">{label}</div>
              <div style="font-size:12px;color:#666;line-height:1.5">{desc}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
