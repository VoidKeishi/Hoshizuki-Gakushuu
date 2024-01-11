import streamlit as st

st.set_page_config(
  page_title="Homepage",
  page_icon="👋"
)

add_logo = st.sidebar.markdown("<a href='http://localhost:8501' target='_self'>Hoshizuki Gakushuu</a>", unsafe_allow_html=True)

with open('style.css') as styleSheet:
  st.markdown(f'<style>{styleSheet.read()}</style>', unsafe_allow_html=True)

st.write("# Welcome to Hoshizuki Gakushuu! 👋")

st.markdown(
    """
    Hoshizuki Gakushuu - an app utilize the capabilities of Azure and GPT-3.5 Turbo to enhance Japanese language learning through interactive quizzes and lessons in a user-friendly environment.
"""
)

