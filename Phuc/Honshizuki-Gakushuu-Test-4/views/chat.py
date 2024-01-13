# Chat page
import streamlit as st
from features.controller import *
import os
import json

def Chat():
  def load_css():
    with open("static/chat.css", "r") as styleSheet:
      css = f"<style>{styleSheet.read()}</style>"
      st.markdown(css, unsafe_allow_html=True)

  load_css()

  def initialize_state():
    if "createdNewChat" not in st.session_state:
      st.session_state["createdNewChat"] = False
      st.session_state["onClickGenerateChat"] = False
      st.session_state["currentChat"] = ""
  initialize_state() 

  contentOfAction = {
    "Translate": "You are an assistant bot that help translate Japanese",
    "Learn Reading": "You are a teacher that teach Japanese. You provide reading lesson for all kind of JLPT level",
    "Translate Image": "You are an assistant bot that read image that has Japanese text on it and translate those words"
  }

  actionOption = st.sidebar.selectbox(
    "Choose what you would like to do ?",
    ["Translate", "Learn Reading", "Translate Image"],
    index=None
  )

  st.sidebar.text_input(
    label="Enter chat name",
    key="chat_name"
  )

  def generateNewChat():
    st.session_state["createdNewChat"] = True
    st.session_state["onClickGenerateChat"] = True
    st.session_state["currentChat"] = st.session_state["chat_name"]

  generateChat = st.sidebar.button(
    label="Create new chat",
    disabled= False if actionOption != None and st.session_state.chat_name != "" else True,
    on_click=generateNewChat,
  )

  def viewChatHistory(filename):
    st.session_state["currentChat"] = filename.split('.')[0]
    with open(os.path.join(os.getcwd(), "samples\\chat-history", filename), 'r') as json_file:
      json_data = json.load(json_file)
      print(json_data)
      st.session_state["conversationsChat"] = json_data
  
  def deleteChatHistory(filename):
    json_file = os.path.join(os.getcwd(), "samples\\chat-history", filename)
    os.remove(json_file)
    if filename.split('.')[0] == st.session_state["currentChat"]:
      st.session_state["currentChat"] = ""
      st.session_state["createdNewChat"] = False

  chat_column = st.columns([4, 2], gap='medium')

  with chat_column[1]:
      history_chat = st.container()
      with history_chat:
        st.markdown("# Your Chat History")
        filenames = os.listdir(os.path.join(os.getcwd(), "samples/chat-history"))
        for filename in filenames:
            with st.container():
              st.write(filename.split('.')[0])
              button_col = st.columns([1, 1])
              with button_col[0]:
                st.button("View", key="viewChatBtn" + filename.split('.')[0], on_click=viewChatHistory, args=(filename, ))
              with button_col[1]:
                st.button("Delete", key="deleteChatBtn" + filename.split('.')[0], on_click=deleteChatHistory, args=(filename, ))

  if st.session_state["createdNewChat"] or st.session_state["currentChat"] != "":
    def initialize_chat_state():
        if "conversationsChat" not in st.session_state or st.session_state["onClickGenerateChat"]:
          st.session_state["conversationsChat"] = [{"role": "system", "content": contentOfAction[actionOption]}]
          st.session_state["onClickGenerateChat"] = False

    initialize_chat_state()
    output_dir = os.path.join(os.getcwd(), "samples/chat-history")
    output_filename = f"{st.session_state['currentChat']}.json"
    output_filename = os.path.join(output_dir, output_filename)

    def on_click_callback():
      human_prompt = st.session_state.human_prompt
      st.session_state.human_prompt = ""
      st.session_state.conversationsChat.append({"role": "user", "content": human_prompt})
      chatNihongo.chatNihongo()
      with open(output_filename, "w") as json_file:
        json.dump(st.session_state.conversationsChat, json_file, indent=2)


    with chat_column[0]:
      st.title("Let's learn Japanese")
      chat_placeholder = st.container()
      with chat_placeholder:
        for chat in st.session_state.conversationsChat:
          if chat["role"] != "system":
            chatMessage = chat["content"]
            div = f"""
              <div class="chat-row {'' if chat["role"] == "assistant" else "row-reverse"}">
                <div class="chat-bubble {'ai-bubble' if chat["role"] == "assistant" else "human-bubble"}">
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
      prompt_placeholder = st.form("chat-form")
      with prompt_placeholder:
        st.markdown(prompt_title, unsafe_allow_html=True)
        cols = st.columns((6, 1))
        cols[0].text_input(
          "Chat",
          label_visibility="collapsed",
          key="human_prompt"
        )
        cols[1].form_submit_button(
          "Submit",
          type="primary",
          on_click=on_click_callback
        )