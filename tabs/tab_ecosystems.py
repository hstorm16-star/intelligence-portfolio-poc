"""
tabs/tab_ecosystems.py
Threat ecosystems tab.
"""

import streamlit as st
from utils.data_loader import load_ecosystems


def render() -> None:
    st.markdown("### Adversarial financial ecosystems investigated")

    ecosystems = load_ecosystems()
    for eco in ecosystems:
        tags_html = "".join(
            f'<span class="eco-tag">{t}</span>' for t in eco["themes"]
        )
        dot_color = eco["color"]
        st.markdown(
            f"""
            <div class="eco-card">
              <div style="display:flex;align-items:flex-start;gap:10px;margin-bottom:8px">
                <div style="width:10px;height:10px;border-radius:50%;background:{dot_color};
                            margin-top:4px;flex-shrink:0"></div>
                <div>
                  <div class="eco-title">{eco['title']}</div>
                  <div class="eco-sub">{eco['description']}</div>
                </div>
              </div>
              <div class="eco-tags">{tags_html}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
