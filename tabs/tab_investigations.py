"""
tabs/tab_investigations.py
Representative operational work tab.
"""

import streamlit as st
from utils.data_loader import load_investigations


def render() -> None:
    st.markdown("### Representative operational work")
    st.markdown(
        '<p class="section-note">Anonymised investigative summaries — no confidential identifiers, '
        "sensitive case details, or counterparty information disclosed.</p>",
        unsafe_allow_html=True,
    )

    investigations = load_investigations()
    for inv in investigations:
        tags_html = "".join(
            f'<span class="rep-tag">{t}</span>' for t in inv["themes"]
        )
        st.markdown(
            f"""
            <div class="rep-card">
              <div class="rep-head">
                <div class="rep-title">{inv['title']}</div>
                <div class="rep-type">{inv['type']}</div>
              </div>
              <div class="rep-body">{inv['body']}</div>
              <div class="rep-tags">{tags_html}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
