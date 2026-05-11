"""
utils/styles.py
Global CSS injected once at app startup.
"""

import streamlit as st


def inject_global_css() -> None:
    st.markdown(
        """
        <style>
        /* ── Layout ─────────────────────────────────────────── */
        .block-container { padding-top: 1.8rem; padding-bottom: 2rem; max-width: 860px; }
        h1 { font-size: 1.45rem !important; font-weight: 600 !important; letter-spacing: -0.3px; }
        h2 { font-size: 1.1rem !important; font-weight: 600 !important; }
        h3 { font-size: 0.95rem !important; font-weight: 600 !important; }

        /* ── Header block ────────────────────────────────────── */
        .port-type  { font-size: 11px; text-transform: uppercase; letter-spacing: 0.8px;
                      color: #888; font-weight: 600; margin-bottom: 4px; }
        .port-title { font-size: 22px; font-weight: 700; letter-spacing: -0.4px; margin-bottom: 4px; }
        .port-name  { font-size: 13px; color: #888; margin-bottom: 10px; }
        .port-tags  { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 4px; }
        .port-tag   { font-size: 11px; padding: 3px 10px; border-radius: 4px; font-weight: 500;
                      border: 1px solid #ddd; color: #555; background: #f7f7f7; }

        /* ── Workstream rows ─────────────────────────────────── */
        .ws-row     { display: flex; align-items: flex-start; gap: 12px;
                      padding: 10px 0; border-bottom: 1px solid #f0f0f0; }
        .ws-row:last-child { border-bottom: none; }
        .ws-label   { font-size: 13px; font-weight: 600; margin-bottom: 3px; }
        .ws-desc    { font-size: 12px; color: #666; line-height: 1.5; }

        /* ── Eco cards ───────────────────────────────────────── */
        .eco-card   { border: 1px solid #e8e8e8; border-radius: 10px;
                      padding: 16px 18px; margin-bottom: 12px; }
        .eco-title  { font-size: 13px; font-weight: 600; margin-bottom: 6px; }
        .eco-sub    { font-size: 12px; color: #666; line-height: 1.55; margin-bottom: 10px; }
        .eco-tags   { display: flex; flex-wrap: wrap; gap: 5px;
                      padding-top: 10px; border-top: 1px solid #f0f0f0; }
        .eco-tag    { font-size: 11px; padding: 2px 9px; border-radius: 3px; font-weight: 500;
                      border: 1px solid #e0e0e0; color: #555; background: #fafafa; }

        /* ── Rep investigation cards ─────────────────────────── */
        .rep-card   { border: 1px solid #e8e8e8; border-radius: 10px;
                      padding: 16px 18px; margin-bottom: 12px; }
        .rep-head   { display: flex; align-items: flex-start;
                      justify-content: space-between; gap: 10px; margin-bottom: 8px; }
        .rep-title  { font-size: 13px; font-weight: 600; flex: 1; }
        .rep-type   { font-size: 10px; font-weight: 600; padding: 2px 9px; border-radius: 3px;
                      border: 1px solid #e0e0e0; color: #666; white-space: nowrap; }
        .rep-body   { font-size: 12px; color: #666; line-height: 1.6; margin-bottom: 8px; }
        .rep-tags   { display: flex; flex-wrap: wrap; gap: 4px; }
        .rep-tag    { font-size: 11px; padding: 2px 8px; border-radius: 3px; font-weight: 500;
                      border: 1px solid #e0e0e0; color: #555; background: #fafafa; }

        /* ── Methodology cards ───────────────────────────────── */
        .meth-card  { border: 1px solid #e8e8e8; border-radius: 8px;
                      padding: 12px 14px; height: 100%; }
        .meth-title { font-size: 12px; font-weight: 600; margin-bottom: 5px; }
        .meth-body  { font-size: 12px; color: #666; line-height: 1.5; }

        /* ── Fusion workflow ─────────────────────────────────── */
        .flow-wrap  { display: flex; align-items: stretch; gap: 0; flex-wrap: wrap; }
        .flow-step  { flex: 1; min-width: 90px; padding: 12px 10px; text-align: center;
                      border: 1px solid #e8e8e8; font-size: 12px; }
        .flow-step:first-child { border-radius: 8px 0 0 8px; }
        .flow-step:last-child  { border-radius: 0 8px 8px 0; }
        .flow-step-title { font-weight: 600; margin-bottom: 4px; }
        .flow-step-sub   { font-size: 11px; color: #888; }
        .flow-arr   { display: flex; align-items: center;
                      padding: 0 4px; color: #aaa; font-size: 14px; }

        /* ── Impact items ────────────────────────────────────── */
        .imp-row    { display: flex; gap: 12px; padding: 10px 0;
                      border-bottom: 1px solid #f0f0f0; align-items: flex-start; }
        .imp-row:last-child { border-bottom: none; }
        .imp-icon   { font-size: 16px; flex-shrink: 0; margin-top: 2px; }
        .imp-text   { font-size: 13px; line-height: 1.5; flex: 1; }
        .imp-badge  { font-size: 10px; font-weight: 600; padding: 2px 9px; border-radius: 3px;
                      border: 1px solid #e0e0e0; color: #666; white-space: nowrap; flex-shrink: 0; }

        /* ── Portfolio narrative blocks ──────────────────────── */
        .ps-block   { border-left: 3px solid #aaa; padding: 10px 14px;
                      background: #f9f9f9; border-radius: 0 8px 8px 0; margin-bottom: 10px; }
        .ps-role    { font-size: 11px; font-weight: 600; color: #888; margin-bottom: 4px;
                      text-transform: uppercase; letter-spacing: 0.4px; }
        .ps-text    { font-size: 13px; line-height: 1.65; }

        /* ── Tool rows ───────────────────────────────────────── */
        .tool-row   { display: flex; align-items: center; gap: 14px;
                      padding: 9px 0; border-bottom: 1px solid #f0f0f0; }
        .tool-row:last-child { border-bottom: none; }
        .tool-name  { font-size: 13px; font-weight: 600; width: 200px; flex-shrink: 0; }
        .tool-desc  { font-size: 12px; color: #666; flex: 1; }
        .tool-bar   { width: 90px; height: 4px; background: #eee; border-radius: 2px; flex-shrink: 0; }
        .tool-fill  { height: 4px; border-radius: 2px; background: #b0b0b0; }

        /* ── Timeline ────────────────────────────────────────── */
        .tl-wrap    { display: flex; gap: 14px; margin-bottom: 14px; }
        .tl-dot-col { display: flex; flex-direction: column; align-items: center; }
        .tl-dot     { width: 10px; height: 10px; border-radius: 50%; margin-top: 4px;
                      flex-shrink: 0; background: #bbb; }
        .tl-line    { width: 1px; flex: 1; background: #e8e8e8; margin-top: 4px; }
        .tl-content { flex: 1; padding-bottom: 8px; }
        .tl-date    { font-size: 11px; color: #999; margin-bottom: 2px; }
        .tl-title   { font-size: 13px; font-weight: 600; }
        .tl-detail  { font-size: 12px; color: #666; margin-top: 3px; line-height: 1.5; }

        /* ── Misc ────────────────────────────────────────────── */
        .anon-ok    { color: #3B6D11; font-size: 13px; }
        .anon-no    { color: #A32D2D; font-size: 13px; }
        .section-note { font-size: 12px; color: #888; margin-bottom: 14px; line-height: 1.6; }
        </style>
        """,
        unsafe_allow_html=True,
    )
