from features import *

def Learn():
    import os
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

    st.sidebar.button( "😃Japanese Quiz", on_click=openFeature, args=("openMakeQuiz",))

    st.sidebar.button("💬Chat", on_click=openFeature, args=("openChat",))

    st.sidebar.button( "📗Dictionary", on_click=openFeature, args=("openDictionary",))

    st.sidebar.write('---')

    filenames = os.listdir(os.path.join(os.getcwd(), "samples"))

    if st.session_state["openMakeQuiz"]:
        jlptLevel = st.sidebar.selectbox(
            "Choose your level",
            ("N5", "N4", "N3", "N2", "N1"),
        )
        quizFile = st.sidebar.selectbox(
            label="Choose quiz",
            options=filenames,
            index=None
        )
        if quizFile:
            showQuiz.showQuiz(quizFile)
        st.sidebar.button("Generate Quiz", on_click=makeQuiz.makeQuiz, args=(jlptLevel, ))
    if st.session_state["openChat"]:
        chat.chat()
        st.sidebar.download_button(
            "Export Chat", convertObjectToString.convertObjectToString(st.session_state["conversationsChat"]))
    if st.session_state["openDictionary"]:
        dictionary.dictionary()
        st.sidebar.download_button(
            "Export Dictionary", convertObjectToString.convertObjectToString(st.session_state["conversationsDictionary"]))
    