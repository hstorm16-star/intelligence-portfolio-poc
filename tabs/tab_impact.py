"""
tabs/tab_impact.py
Strategic impact and industry engagement tab.
"""

import streamlit as st
from utils.data_loader import load_impact


INDUSTRY = [
    ("TRM Customer Connect webinar · Jun 2025",
     '"Intelligence Fusion, Typology Building, and Service Risk Assessments" — '
     "practitioner voice to TRM's global customer audience on advanced blockchain intelligence methodology."),
    ("Guest lecturer · University of Waikato · Jul 2023",
     'DIGIB302 — "Blockchain in the Digital World" · academic practitioner engagement.'),
    ("Chainalysis top community contributor",
     "Recognised by Chainalysis for knowledge contribution to the blockchain intelligence practitioner community."),
]


def render() -> None:
    st.markdown("### Evidence of impact")

        impact_items = load_impact()

    for item in impact_items:
        st.markdown(
            f"""
            <div style="border:1px solid #e8e8e8;border-radius:10px;padding:14px 18px;margin-bottom:10px">
                <div style="font-size:18px;margin-bottom:6px">{item['icon']} <b>{item['badge']}</b></div>
                <div style="font-size:15px;line-height:1.5">{item['text']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
            </div>
            """,
            unsafe_allow_html=True,
        )
