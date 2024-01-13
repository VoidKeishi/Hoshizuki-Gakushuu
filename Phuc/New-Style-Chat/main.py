import streamlit as st
from openai import AzureOpenAI

def load_css():
  with open("static/style.css", "r") as styleSheet:
    css = f"<style>{styleSheet.read()}</style>"
    st.markdown(css, unsafe_allow_html=True)

load_css()

client = AzureOpenAI(
  api_key = "16ed8a71e992441f98be936d5767fea4",  
  api_version = "2023-05-15",
  azure_endpoint = "https://sunhackathon22.openai.azure.com/"  # Your Azure OpenAI resource's endpoint value.
)

def on_click_callback():
  human_prompt = st.session_state.human_prompt
  st.session_state.history.append({"role": "user", "message": human_prompt})
  response = client.chat.completions.create(
            model="GPT35TURBO", # model = "deployment_name".
            messages=st.session_state.conversations
  )
  full_response = response.choices[0].message.content
  st.session_state.history.append({"role": "assistant", "message": full_response})

def initialize_session_state():
  if "history" not in st.session_state:
    st.session_state["history"] = []
  if "conversations" not in st.session_state:
    st.session_state.conversations = [{"role": "system", "content": "You are a brilliant teacher that teach Japanese and you always provide high quality quiz and answer"}]

initialize_session_state()

st.title('Hello Custom CSS Chatbot')

chat_placeholder = st.container()
prompt_placeholder = st.form("chat-form")
credit_card_placeholder = st.empty()

with chat_placeholder:
  for chat in st.session_state.history:
    if chat["role"] != "system":
      chatMessage = chat["message"]
      div = f"""
        <div class="chat-row
        {'' if chat["role"] == "assistant" else "row-reverse"}">
          <img class="chat-icon" src="app/static/{'robot.png' if chat["role"] == "assistant"
                                else 'people.png'}"
                width=32 height=32>
          <div class="chat-bubble
          {'ai-bubble' if chat["role"] == "assistant" else "human-bubble"}">
            &#8203;{chatMessage}
          </div>
        </div>
      """
      st.markdown(div, unsafe_allow_html=True)

prompt_title = f"""
  <div class="prompt-title">
    <span class="prompt-title">Chat</span>
    <span class="prompt-action">- press Enter to chat </span>
  </div>
"""
with prompt_placeholder:
  st.markdown(prompt_title, unsafe_allow_html=True)
  cols = st.columns((6, 1))
  cols[0].text_input(
    "Chat",
    value="Hello bot",
    label_visibility="collapsed",
    key="human_prompt"
  )
  cols[1].form_submit_button(
    "Submit",
    type="primary",
    on_click=on_click_callback
  )