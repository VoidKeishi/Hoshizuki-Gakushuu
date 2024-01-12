import streamlit as st
from openai import AzureOpenAI

client = AzureOpenAI(
  api_key = "16ed8a71e992441f98be936d5767fea4",  
  api_version = "2023-05-15",
  azure_endpoint = "https://sunhackathon22.openai.azure.com/"  # Your Azure OpenAI resource's endpoint value.
)

if "conversations" not in st.session_state:
    st.session_state.conversations = [{"role": "system", "content": "You are a brilliant teacher that teach Japanese and you always provide high quality quiz and answer"}]

for conversation in st.session_state.conversations:
    if conversation["role"] != "system":
      with st.chat_message(conversation["role"]):
          st.markdown(conversation["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.conversations.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        response = client.chat.completions.create(
            model="GPT35TURBO", # model = "deployment_name".
            messages=st.session_state.conversations
        )
        full_response = response.choices[0].message.content
        message_placeholder.markdown(full_response)
    st.session_state.conversations.append({"role": "assistant", "content": full_response})