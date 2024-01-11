import streamlit as st
import makeQuiz
import chat
import dictionary

st.set_page_config(
  page_title="Hoshizuki Gakushuu",
  page_icon="🇯🇵"
)

with open('style.css') as styleSheet:
  st.markdown(f'<style>{styleSheet.read()}</style>', unsafe_allow_html=True)

allPages = ["openMakeQuiz", "openChat", "openDictionary"]

for page in allPages:
  if page not in st.session_state:
    st.session_state[page] = False

def openFeature(pageName):
  for page in allPages:
    if (page == pageName):
      st.session_state[page] = True 
    else:
      st.session_state[page] = False

add_logo = st.sidebar.markdown("<a href='http://localhost:8501' target='_self'>Hoshizuki Gakushuu</a>", unsafe_allow_html=True)

add_make_quiz = st.sidebar.button("😃Japanese Quiz", on_click=openFeature, args=("openMakeQuiz",))

add_chat = st.sidebar.button("💬Chat", on_click=openFeature, args=("openChat",))

add_dictionary = st.sidebar.button("📗Dictionary", on_click=openFeature, args=("openDictionary",))

if st.session_state["openMakeQuiz"]:
  makeQuiz.makeQuiz()
  print(st.session_state['conversationsQuiz'])
if st.session_state["openChat"]:
  chat.chat()
if st.session_state["openDictionary"]:
  dictionary.dictionary()

