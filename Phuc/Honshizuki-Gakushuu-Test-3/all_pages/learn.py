from features import *

def Learn():
    import streamlit as st
    from utils import convertObjectToString
    
    print("Learn page is rendering...\n")
    with open('assets/learn.css') as styleSheet:
        st.markdown(f'<style>{styleSheet.read()}</style>', unsafe_allow_html=True)

    allFeatures = ["openMakeQuiz", "openChat", "openDictionary"]

    for feature in allFeatures:
        if feature not in st.session_state:
            st.session_state[feature] = False


    def openFeature(featureName):
        print("Clicked on feature: " + featureName)
        for feature in allFeatures:
            if (feature == featureName):
                st.session_state[feature] = True
            else:
                st.session_state[feature] = False


    

    add_make_quiz = st.sidebar.button(
        "😃Japanese Quiz", on_click=openFeature, args=("openMakeQuiz",))

    add_chat = st.sidebar.button("💬Chat", on_click=openFeature, args=("openChat",))

    add_dictionary = st.sidebar.button(
        "📗Dictionary", on_click=openFeature, args=("openDictionary",))

    if st.session_state["openMakeQuiz"]:
        makeQuiz.makeQuiz()
        add_export_button = st.sidebar.download_button(
            "Export Quiz", convertObjectToString.convertObjectToString(st.session_state["conversationsQuiz"]))
    if st.session_state["openChat"]:
        chat.chat()
        add_export_button = st.sidebar.download_button(
            "Export Chat", convertObjectToString.convertObjectToString(st.session_state["conversationsChat"]))
    if st.session_state["openDictionary"]:
        dictionary.dictionary()
        add_export_button = st.sidebar.download_button(
            "Export Dictionary", convertObjectToString.convertObjectToString(st.session_state["conversationsDictionary"]))
