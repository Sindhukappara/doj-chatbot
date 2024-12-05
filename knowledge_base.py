import streamlit as st
import json
import os

def load_knowledge_base():
    try:
        if 'knowledge_base' not in st.session_state:
            with open('doj_knowledge.jsonl', 'r', encoding='utf-8') as f:
                st.session_state.knowledge_base = json.load(f)
        return st.session_state.knowledge_base
    except FileNotFoundError:
        st.error("Knowledge base file (doj_knowledge.json) not found")
        return {}
