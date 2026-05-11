"""
app.py
Threat Finance & Sanctions Investigations — Intelligence Portfolio
Proof-of-concept portfolio dashboard. Run with:
    python3 -m streamlit run app.py
"""

import streamlit as st

from utils.styles import inject_global_css
from tabs import (
    tab_overview,
    tab_ecosystems,
    tab_investigations,
    tab_methodology,
    tab_technical,
    tab_background,
    tab_impact,
)

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Intelligence Portfolio — George Hale",
    page_icon="🔍",
    layout="centered",
    initial_sidebar_state="collapsed",
)

inject_global_css()

# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="port-type">Intelligence portfolio</div>
    <div class="port-title">Threat Finance &amp; Sanctions Investigations</div>
    <div class="port-name">
      George Hale · Intelligence analyst · Binance CIFC ·
      Prior NZ Police virtual assets specialist
    </div>
    <div class="port-tags">
      <span class="port-tag">Sanctions nexus</span>
      <span class="port-tag">Adversarial financial networks</span>
      <span class="port-tag">Intelligence fusion</span>
      <span class="port-tag">Cross-chain tracing</span>
      <span class="port-tag">ACAMS CCAS · Chainalysis CISC · TRM ACE</span>
      <span class="port-tag">5+ yr experience</span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")

# ── Navigation ─────────────────────────────────────────────────────────────────
TAB_LABELS = [
    "Overview",
    "Threat ecosystems",
    "Representative work",
    "Methodology",
    "Technical",
    "Background",
    "Strategic impact",
    "Portfolio framing",
]

tabs = st.tabs(TAB_LABELS)

with tabs[0]:
    tab_overview.render()

with tabs[1]:
    tab_ecosystems.render()

with tabs[2]:
    tab_investigations.render()

with tabs[3]:
    tab_methodology.render()

with tabs[4]:
    tab_technical.render()

with tabs[5]:
    tab_background.render()

with tabs[6]:
    tab_impact.render()


# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    '<p style="font-size:11px;color:#bbb;text-align:center">'
    "Proof-of-concept portfolio dashboard · All data sanitised · No confidential information disclosed"
    "</p>",
    unsafe_allow_html=True,
)
