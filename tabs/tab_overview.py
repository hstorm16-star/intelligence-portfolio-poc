"""
tabs/tab_overview.py
Overview tab — investigative scope and domain summary.
"""

import streamlit as st
from utils.data_loader import load_workstreams


def render() -> None:
    st.markdown("### Investigative scope")

    workstreams = load_workstreams()
    for ws in workstreams:
        bar_pct = ws["depth"]
        st.markdown(
            f"""
            <div class="ws-row">
              <div style="flex:1">
                <div class="ws-label">{ws['label']}</div>
                <div class="ws-desc">{ws['description']}</div>
                <div style="margin-top:8px;height:4px;background:#eee;border-radius:2px;width:100%">
                  <div style="height:4px;border-radius:2px;background:#b0b0b0;width:{bar_pct}%"></div>
                </div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown("### Intelligence domains at a glance")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            <div style="border:1px solid #e8e8e8;border-radius:10px;padding:16px 18px">
              <div style="font-size:13px;font-weight:600;margin-bottom:10px">Sanctions &amp; state-linked</div>
              <div style="font-size:12px;color:#666;display:flex;flex-direction:column;gap:6px">
                <div>Iran — oil procurement · VASP rotation · OFAC evasion</div>
                <div>Russia — Garantex-adjacent · nested exchangers · RUB flows</div>
                <div>DPRK — IT worker ecosystem · cross-chain laundering</div>
                <div>Myanmar · Venezuela — cross-border procurement exposure</div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div style="border:1px solid #e8e8e8;border-radius:10px;padding:16px 18px">
              <div style="font-size:13px;font-weight:600;margin-bottom:10px">Threat finance &amp; cybercrime</div>
              <div style="font-size:12px;color:#666;display:flex;flex-direction:column;gap:6px">
                <div>Terrorist financing — attribution · network tracing</div>
                <div>Scattered Spider-related — infrastructure analysis</div>
                <div>Huione / Xinbi — guarantee system · illicit payment rails</div>
                <div>Dual-use procurement — drone · logistics · supply chain</div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
