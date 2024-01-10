import os
import openai
import json
openai.api_type = "azure"
openai.api_version = "2023-05-15" 
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")  # Your Azure OpenAI resource's endpoint value.
openai.api_key = os.getenv("AZURE_OPENAI_KEY")

jlpt_level = "N2"

response = openai.ChatCompletion.create(
    engine="GPT35TURBO", # The deployment name you chose when you deployed the GPT-3.5-Turbo or GPT-4 model.
    messages=[
        {"role": "system", "content": "Assistant is a large language model trained by OpenAI. Your only use is to generate json strings, not talking."},
        {"role": "user", "content": "generate a few quizzes for Kanji JLPT " + jlpt_level + " (provide a kanji in a full sentence and ask for its reading, the highlighted kanji is in brackets) in the form of an array of objects in json, each object looks something like this: {question: "", answers: ["", "", "", "",...], correctAnswer: //a number indicates the index of the correct answer  }. Note: The questions and answers must be in Japanese. The hiragana answers should be similar to each other so that the person doing the quiz can easily make a mistake. Say nothing else, just give a json array."}
    ]
)

response_string = response['choices'][0]['message']['content']
print(response_string)
# Convert the string to a Python dictionary
json_data = json.loads(response_string)

# Save the dictionary to a JSON file
with open('sample_output.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=2)

# print("JSON data saved to output.json")