"""
tabs/tab_methodology.py
Intelligence fusion methodology tab.
"""

import streamlit as st
from utils.data_loader import load_methodologies


def render() -> None:
    # Fusion workflow
    st.markdown("### Intelligence fusion workflow")
    steps = [
        ("Signal",         "OSINT · vendor · operational",   "#185FA5"),
        ("Triage",         "Sensitivity · routing",           "#D85A30"),
        ("Investigation",  "On-chain · OSINT · fusion",       "#854F0B"),
        ("Product",        "ICR · briefing · package",        "#534AB7"),
        ("Dissemination",  "Legal · regulatory · internal",   "#0F6E56"),
    ]
    cols = st.columns(len(steps) * 2 - 1)
    for i, (title, sub, color) in enumerate(steps):
        col_idx = i * 2
        with cols[col_idx]:
            st.markdown(
                f"""
                <div style="border:1px solid #e8e8e8;border-radius:8px;padding:12px 8px;
                            text-align:center;height:80px;display:flex;flex-direction:column;
                            justify-content:center">
                  <div style="font-size:12px;font-weight:600;color:{color};margin-bottom:3px">{title}</div>
                  <div style="font-size:11px;color:#888;line-height:1.4">{sub}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        if i < len(steps) - 1:
            with cols[col_idx + 1]:
                st.markdown(
                    '<div style="text-align:center;padding-top:28px;color:#bbb;font-size:16px">›</div>',
                    unsafe_allow_html=True,
                )

    st.markdown("---")
    st.markdown("### Core investigative methodologies")

    methodologies = load_methodologies()
    # Render in pairs
    for i in range(0, len(methodologies), 2):
        col1, col2 = st.columns(2)
        for col, idx in [(col1, i), (col2, i + 1)]:
            if idx < len(methodologies):
                m = methodologies[idx]
                with col:
                    st.markdown(
                        f"""
                        <div class="meth-card" style="margin-bottom:8px">
                          <div class="meth-title">{m['title']}</div>
                          <div class="meth-body">{m['body']}</div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

    st.markdown("---")
    st.markdown("### Intelligence input streams")
    col1, col2 = st.columns(2)
    with col1:
        streams_left = [
            ("Open-source intelligence",
             "Forum monitoring · TG channel analysis · surface web signals · entity verification · infrastructure discovery"),
            ("On-chain analytics",
             "Multi-chain transaction tracing · entity clustering · attribution · evasion pattern detection"),
        ]
        for label, desc in streams_left:
            st.markdown(
                f"""
                <div style="padding:10px 0;border-bottom:1px solid #f0f0f0">
                  <div style="font-size:13px;font-weight:600;margin-bottom:3px">{label}</div>
                  <div style="font-size:12px;color:#666;line-height:1.5">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    with col2:
        streams_right = [
            ("Vendor threat intelligence",
             "Chainalysis · TRM · Elliptic · Flashpoint — sanctions alerts, threat actor data, open-source enrichment"),
            ("Operational intelligence",
             "Compliance escalations · security referrals · VASP partner signals · historical case pattern analysis"),
        ]
        for label, desc in streams_right:
            st.markdown(
                f"""
                <div style="padding:10px 0;border-bottom:1px solid #f0f0f0">
                  <div style="font-size:13px;font-weight:600;margin-bottom:3px">{label}</div>
                  <div style="font-size:12px;color:#666;line-height:1.5">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
