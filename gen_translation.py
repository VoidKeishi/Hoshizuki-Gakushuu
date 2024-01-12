import openai
import datetime
openai.api_type = "azure"
openai.api_version = "2023-05-15" 
openai.api_base = ("https://sunhackathon22.openai.azure.com/")  # Your Azure OpenAI resource's endpoint value.
openai.api_key = ('16ed8a71e992441f98be936d5767fea4')

def get_completion_translate(text, model="GPT35TURBO16K"):
    prompt = f"""
    Translate the following text to Japanense and say nothing \
    : ```{text}```
    """
    messages = [
        {"role": "system", "content": "You are a Japanese language translation expert."},
        {"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        engine=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

text_translate = input()

response = get_completion_translate(text_translate)
print(response)

# ISSUES: 
# 1. The answers sometimes contain kanji
# 2. The answers are not similar to each other
# 3. The answers are in katakana
# 4. Some answers are exactly the same