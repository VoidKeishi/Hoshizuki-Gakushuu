from openai import AzureOpenAI

def exclude_forbidden_characters(file_name):
    forbidden_chars = r'\/:*?"<>|'  # Forbidden characters
    cleaned_name = ''.join(char for char in file_name if char not in forbidden_chars)
    return cleaned_name


def generateRandomName(initialConversation):
  client = AzureOpenAI(
        api_key="16ed8a71e992441f98be936d5767fea4",
        api_version="2023-05-15",
        # Your Azure OpenAI resource's endpoint value.
        azure_endpoint="https://sunhackathon22.openai.azure.com/"
    )
  
  initialConversation = initialConversation[1:]
  fullConversation = ""
  for conversation in initialConversation:
    fullConversation += conversation["role"] + ": " + conversation["content"] + "\n"

  response = client.chat.completions.create(
    model="GPT35TURBO", # model = "deployment_name".
    messages=[
        {"role": "system", "content": """Assistant is a large language model trained by OpenAI.
          Your mission is to only name the input conversation. Given a conversation, you must only give it a name.
          Just name it, no talking.                         
         """},
        {"role": "user", "content": f"I have the following conversation \n {fullConversation} \n How should I name this conversation ?"}
    ]
  )
  return exclude_forbidden_characters(response.choices[0].message.content)
