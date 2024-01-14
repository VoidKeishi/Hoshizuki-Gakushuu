import streamlit as st
from streamlit_option_menu import option_menu
from features import *
from views import *

st.set_page_config(
  page_title="Hoshizuki Gakushuu",
  page_icon="🇯🇵",
)

# def load_css():
#   with open("static/main.css", "r") as styleSheet:
#     css = f"<style>{styleSheet.read()}</style>"
#     st.markdown(css, unsafe_allow_html=True)

# load_css()

with st.sidebar:
  st.write(f"# Japanese Learning App")
  optionMenu = option_menu(
  menu_title=None,
  options=["Home", "Learn", "Chat", "About Us"],
)

print("Main page is rendering....\n")

if optionMenu == "Home":
  home.Home()
if optionMenu == "Learn":
  learn.Learn()
if optionMenu == "Chat":
  chat.Chat()