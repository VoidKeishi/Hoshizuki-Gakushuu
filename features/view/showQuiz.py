def showQuiz(quizFile):
    import streamlit as st
    import os
    import json

    def showResult(userAnswer, quizAnswer):
        if userAnswer == quizAnswer:
            st.write('Đúng')
        else:
            st.write("Đáp án đúng: " + quizAnswer)

    # st.write("Hãy chọn 1 đáp án đúng trong các câu hỏi sau")
    st.markdown("""
        # Hãy chọn 1 đáp án đúng trong các câu hỏi sau
    """)

    filenames = os.listdir(os.path.join(os.getcwd(), "samples"))
    for filename in filenames:
        if filename.endswith(".json"):
            if filename == quizFile:
                with open(os.path.join(os.getcwd(), "samples", filename), 'r') as json_file:
                    json_data = json.load(json_file)
                    for quiz in json_data:
                        print("Câu hỏi: " + quiz['question'], end="\n\n")
                        print("Các đáp án:" + str(quiz['answers']), end="\n\n")
                        print("Đáp án đúng:" + quiz['answers']
                            [quiz['correctAnswer']], end="\n\n")
                        print("===========================================", end="\n\n")

                        question = quiz['question']

                        with st.container():
                            st.markdown(f"#### {question}")
                            userAnswer = st.radio(
                                label="Nothing",
                                options=[quiz['answers'][0], quiz['answers'][1],
                                    quiz['answers'][2], quiz['answers'][3]],
                                index=None,
                                key=question,
                                label_visibility='collapsed'
                            )
                            if userAnswer:
                                showResult(userAnswer, quiz['answers'][quiz['correctAnswer']])
