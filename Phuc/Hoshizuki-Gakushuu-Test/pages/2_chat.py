import streamlit as st
from openai import AzureOpenAI

st.set_page_config(page_title="Chat with Japanese teacher")

with open('style.css') as styleSheet:
  st.markdown(f'<style>{styleSheet.read()}</style>', unsafe_allow_html=True)

client = AzureOpenAI(
  api_key = "16ed8a71e992441f98be936d5767fea4",  
  api_version = "2023-05-15",
  azure_endpoint = "https://sunhackathon22.openai.azure.com/"  # Your Azure OpenAI resource's endpoint value.
)

content = "You are a brilliant teacher that teach Japanese. You love to talk about topic concerned with Japan and you always want to talk in detail about the topic"

if "conversationsChat" not in st.session_state:
    st.session_state.conversationsChat = [{"role": "system", "content": content}]

for conversation in st.session_state.conversationsChat:
    if conversation["role"] != "system":
      with st.chat_message(conversation["role"]):
          st.markdown(conversation["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.conversationsChat.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        response = client.chat.completions.create(
            model="GPT35TURBO", # model = "deployment_name".
            messages=st.session_state.conversationsChat
        )
        full_response = response.choices[0].message.content
        message_placeholder.markdown(full_response)
    st.session_state.conversationsChat.append({"role": "assistant", "content": full_response})