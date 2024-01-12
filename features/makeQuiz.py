def makeQuiz(jlptLevel):
    import os
    from openai import AzureOpenAI
    import json
    import datetime

    client = AzureOpenAI(
            api_key = "16ed8a71e992441f98be936d5767fea4",  
            api_version = "2023-05-15",
            azure_endpoint = "https://sunhackathon22.openai.azure.com/"
    )

    # jlptLevel = "N3"
    message_content = {
        "kanji": """generate a few quizzes for Kanji JLPT """ + jlptLevel + 
                                        """ (provide a kanji in a full sentence and ask for its reading, the highlighted kanji is in brackets) in the form of an array of objects in json, 
                                        each object looks something like this: {question: "", answers: ["", "", "", "",...], correctAnswer: //a number indicates the index of the correct answer  }. 
                                        Note: The questions and answers must be in Japanese. 
                                        The hiragana answers should be similar to each other so that the person doing the quiz can easily make a mistake. 
                                        Say nothing else, just give a json array.""",
        "vocabulary": """generate a few quizzes for Vocabulary JLPT """ + jlptLevel + 
                                        """ in the form of an array of objects in json, 
                                        each object looks something like this: {question: "", answers: ["", "", "", "",...], correctAnswer: //a number indicates the index of the correct answer  }. 
                                        Note: The questions and answers must be in Japanese. 
                                        Say nothing else, just give a json array.""",
    }
    response = client.chat.completions.create(
        model="GPT35TURBO", # The deployment name you chose when you deployed the GPT-3.5-Turbo or GPT-4 model.
        messages=[
            {"role": "system", "content": "Assistant is a large language model trained by OpenAI. Your only use is to generate json strings, not talking."},
            {"role": "user", "content": message_content["vocabulary"]}
        ],
        temperature=1
    )

    response_string = response.choices[0].message.content
    print(response_string)
    # Convert the string to a Python dictionary
    json_data = json.loads(response_string)

    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    # just make sure the output filename is unique
    output_filename = f"quiz_{jlptLevel}_{current_datetime}.json"
    output_dir = os.path.join(os.getcwd(), "samples")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_filename = os.path.join(output_dir, output_filename)

    # Save the dictionary to a JSON file
    with open(output_filename, 'w') as json_file:
        json.dump(json_data, json_file, indent=2)