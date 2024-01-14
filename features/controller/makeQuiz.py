def makeQuiz(jlptLevel, topic):
    import os
    from openai import AzureOpenAI
    import json
    import datetime
    import streamlit as st

    client = AzureOpenAI(
        api_key = st.secrets.API_KEY,  
        api_version = st.secrets.API_VERSION,
        azure_endpoint = st.secrets.END_POINT 
    )

    # jlptLevel = "N3"
    message_content = {
        "Kanji": """generate a few quizzes for Kanji JLPT """ + jlptLevel + 
                                            """ (provide a kanji in a full sentence and ask for its reading, the highlighted kanji is in brackets) in the form of an array of objects in json, 
                                            each object looks something like this: {question: "", answers: ["", "", "", "",...], correctAnswer: //a number indicates the index of the correct answer  }. 
                                            Note: The questions and answers must be in Japanese. 
                                            The hiragana answers should be similar to each other so that the person doing the quiz can easily make a mistake. 
                                            Say nothing else, just give a json array.""",
        "Vocabulary": """generate a few quizzes for Vocabulary JLPT """ + jlptLevel + 
                                            """ in the form of an array of objects in json, 
                                            each object looks something like this: {question: "", answers: ["", "", "", "",...], correctAnswer: //a number indicates the index of the correct answer  }. 
                                            Note: The questions and answers must be in Japanese. 
                                            Say nothing else, just give a json array.""",
        "Grammar": """generate a few quizzes for Grammar JLPT """ + jlptLevel + 
                                            """ in the form of an array of objects in json, 
                                            each object looks something like this: {question: "", answers: ["", "", "", "",...], correctAnswer: //a number indicates the index of the correct answer  }. 
                                            Note: The questions and answers must be in Japanese. 
                                            Say nothing else, just give a json array.""",                     
    }
    response = client.chat.completions.create(
        model="GPT35TURBO", # The deployment name you chose when you deployed the GPT-3.5-Turbo or GPT-4 model.
        messages=[
            {"role": "system", "content": "Assistant is a large language model trained by OpenAI. Your only use is to generate json strings, not talking."},
            {"role": "user", "content": message_content[topic]}
        ],
        temperature=1
    )

    response_string = response.choices[0].message.content
    print(response_string)
    # Convert the string to a Python dictionary
    json_data = json.loads(response_string)

    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    # just make sure the output filename is unique
    output_filename = f"{jlptLevel}_{topic}_{current_datetime}_Quiz.json"
    output_dir = os.path.join(os.getcwd(), "samples")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_filename = os.path.join(output_dir, output_filename)

    # Save the dictionary to a JSON file
    with open(output_filename, 'w') as json_file:
        json.dump(json_data, json_file, indent=2)