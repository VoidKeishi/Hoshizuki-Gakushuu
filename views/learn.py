from features.controller import *
from features.view import *

def Learn():
    import os
    import streamlit as st
    from utils import convertObjectToString
    
    print("Learn page is rendering...\n")
    with open('static/learn.css') as styleSheet:
        st.markdown(f'<style>{styleSheet.read()}</style>', unsafe_allow_html=True)

    allFeatures = ["openMakeQuiz", "openChat", "openDictionary"]

    for feature in allFeatures:
        if feature not in st.session_state:
            st.session_state[feature] = False

    def openFeature(featureName):
        print("Clicked on feature: " + featureName)
        print(filenames)
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
            ('N1', 'N2', 'N3', 'N4', 'N5'),
        )
        topic = st.sidebar.selectbox(
            "Choose topic",
            ('Kanji', 'Vocabulary', 'Grammar'),
        )

        # Filter filenames based on the selected level and topic
        filtered_filenames = [name for name in filenames if jlptLevel in name and topic.lower() in name.lower()]
        print(filtered_filenames)
        # Create formatted names with indices for the selected level and topic
        formatted_names_with_indices = [
            f'{jlptLevel} {topic} Quiz #{i+1}' for i, name in enumerate(filtered_filenames)
        ]
        
        # Create a mapping for formatted filenames with indices
        file_name_mapping_with_indices = dict(zip(formatted_names_with_indices, filtered_filenames))

        quizFile = st.sidebar.selectbox(
            label="Choose quiz",
            options=formatted_names_with_indices,
            index=0
        )
        if quizFile:
            fileToShow = file_name_mapping_with_indices[quizFile]
            showQuiz.showQuiz(quizFile=fileToShow)
        st.sidebar.button("Generate Quiz", on_click=makeQuiz.makeQuiz, args=(jlptLevel, topic))
    