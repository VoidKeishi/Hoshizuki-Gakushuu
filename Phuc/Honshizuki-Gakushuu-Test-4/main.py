import streamlit as st
from streamlit_option_menu import option_menu
from features import *
from all_pages import *

st.set_page_config(
  page_title="Hoshizuki Gakushuu",
  page_icon="🇯🇵",
)

with open('assets/main.css') as styleSheet:
        st.markdown(f'<style>{styleSheet.read()}</style>', unsafe_allow_html=True)

with st.sidebar:
  add_logo = st.sidebar.markdown(
        "<a href='http://localhost:8501' target='_self'>Hoshizuki Gakushuu</a>", unsafe_allow_html=True)
  optionMenu = option_menu(
  menu_title=None,
  options=["Home", "Learn", "Daily Vocab", "Summarize", "Conversation History"],
)

print("Main page is rendering....\n")

if optionMenu == "Learn":
  learn.Learn()
if optionMenu == "Home":
  home.Home()