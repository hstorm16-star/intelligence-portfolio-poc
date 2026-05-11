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
    items_html = ""
    for item in impact_items:
        items_html += f"""
        <div class="imp-row">
          <div class="imp-icon">{item['icon']}</div>
          <div class="imp-text">{item['text']}</div>
          <div class="imp-badge">{item['badge']}</div>
        </div>
        """
    st.markdown(
        f'<div style="border:1px solid #e8e8e8;border-radius:10px;padding:8px 16px">'
        f"{items_html}</div>",
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.markdown("### Industry engagement")

    for title, desc in INDUSTRY:
        st.markdown(
            f"""
            <div style="padding:10px 0;border-bottom:1px solid #f0f0f0">
              <div style="font-size:13px;font-weight:600;margin-bottom:3px">{title}</div>
              <div style="font-size:12px;color:#666;line-height:1.5">{desc}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
