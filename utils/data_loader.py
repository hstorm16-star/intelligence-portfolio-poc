"""
utils/data_loader.py
Centralised JSON data loader with caching.
"""

import json
import os
import streamlit as st

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")


def _load(filename: str) -> list | dict:
    path = os.path.join(DATA_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


@st.cache_data
def load_workstreams() -> list:
    return _load("workstreams.json")


@st.cache_data
def load_ecosystems() -> list:
    return _load("ecosystems.json")


@st.cache_data
def load_investigations() -> list:
    return _load("investigations.json")


@st.cache_data
def load_methodologies() -> list:
    return _load("methodologies.json")


@st.cache_data
def load_impact() -> list:
    return _load("impact.json")
