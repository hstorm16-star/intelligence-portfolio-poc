import streamlit as st
from utils.data_loader import load_impact

INDUSTRY = [
    (
        "TRM Customer Connect webinar · Jun 2025",
        "External-facing practitioner presentation on intelligence fusion, typology building, and service risk assessment.",
    ),
    (
        "Guest lecturer · University of Waikato · Jul 2023",
        "Academic practitioner engagement on blockchain intelligence and investigations.",
    ),
    (
        "Chainalysis top community contributor",
        "Recognised by Chainalysis for knowledge contribution to the blockchain intelligence practitioner community.",
    ),
]


def render() -> None:
    st.markdown("### Evidence of impact")

    impact_items = load_impact()

    for item in impact_items:
        icon = item.get("icon", "•")
        text = item.get("text", "")
        badge = item.get("badge", "")

        st.markdown(
            f"""
            <div style="border:1px solid #e8e8e8;border-radius:10px;padding:14px 18px;margin-bottom:10px">
                <div style="font-size:15px;line-height:1.5">{icon} <b>{text}</b></div>
                <div style="font-size:12px;color:#aaa;margin-top:6px">{badge}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown("### Industry engagement")

    for title, desc in INDUSTRY:
        st.markdown(
            f"""
            <div style="padding:10px 0;border-bottom:1px solid #333">
                <div style="font-size:13px;font-weight:600;margin-bottom:3px">{title}</div>
                <div style="font-size:12px;color:#aaa;line-height:1.5">{desc}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
