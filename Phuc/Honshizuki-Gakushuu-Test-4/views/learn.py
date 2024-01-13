from features.controller import *
from features.view import *

def Learn():
    import os
    import streamlit as st
    from utils import convertObjectToString

    # def load_css():
    #     with open("static/learn.css", "r") as styleSheet:
    #         css = f"<style>{styleSheet.read()}</style>"
    #         st.markdown(css, unsafe_allow_html=True)

    # load_css()

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

    st.sidebar.write('---')

    filenames = os.listdir(os.path.join(os.getcwd(), "samples"))

    if st.session_state["openMakeQuiz"]:
        jlptLevel = st.sidebar.selectbox(
            "Choose your level",
            ("N5", "N4", "N3", "N2", "N1"),
        )
        quizFile = st.sidebar.selectbox(
            label="Choose quiz",
            options=filenames[1:],
            index=None
        )
        if quizFile:
            showQuiz.showQuiz(quizFile)
        st.sidebar.button("Generate Quiz", on_click=makeQuiz.makeQuiz, args=(jlptLevel, ))
    