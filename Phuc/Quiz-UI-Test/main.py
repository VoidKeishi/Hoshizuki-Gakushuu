import streamlit as st

import os
import json

def showResult(userAnswer, quizAnswer):
    if  userAnswer == quizAnswer:
        st.write('Đúng')
    else:
        st.write("Đáp án đúng: " + quizAnswer)

filenames = os.listdir(os.path.join(os.getcwd(), "samples"))
for filename in filenames:
    if filename.endswith(".json"):
        with open(os.path.join(os.getcwd(), "samples", filename), 'r') as json_file:
            json_data = json.load(json_file)
            for quiz in json_data:
                print("Câu hỏi: " + quiz['question'], end="\n\n")
                print("Các đáp án:" + str(quiz['answers']), end="\n\n")
                print("Đáp án đúng:" + quiz['answers'][quiz['correctAnswer']], end="\n\n")
                print("===========================================", end="\n\n")

                with st.container():
                    st.write(quiz['question'])
                    userAnswer = st.radio(
                        "Hãy chọn 1 đáp án đúng",
                        [quiz['answers'][0], quiz['answers'][1], quiz['answers'][2], quiz['answers'][3]],
                        index=None
                    )
                    if userAnswer:
                        showResult(userAnswer, quiz['answers'][quiz['correctAnswer']])

st.selectbox(
    label="Choose the option",
    options=["File 1", "File 2", "File 3"]
)
