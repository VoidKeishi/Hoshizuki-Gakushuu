def dictionary():
    import os
    import streamlit as st
    from openai import AzureOpenAI

    client = AzureOpenAI(
        api_key = st.secrets.API_KEY,  
        api_version = st.secrets.API_VERSION,
        azure_endpoint = st.secrets.END_POINT 
    )

    content = "You are a brilliant teacher that teach Japanese. You have an extremely good memory that can memorized Japanese vocab and library, you are the professional of Japanese vocabulary. In addition to providing the meaning of the word, you also provide the kanji and examples sentences"

    if "conversationsDictionary" not in st.session_state:
        st.session_state.conversationsDictionary = [
            {"role": "system", "content": content}]

    for conversation in st.session_state.conversationsDictionary:
        if conversation["role"] != "system":
            with st.chat_message(conversation["role"]):
                st.markdown(conversation["content"])

    if prompt := st.chat_input("What is up?"):
        st.session_state.conversationsDictionary.append(
            {"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            for response in client.chat.completions.create(
                model="GPT35TURBO",  # model = "deployment_name".
                messages=st.session_state.conversationsDictionary,
                stream=True
            ):
                full_response += response.choices[0].delta.content or ""
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        st.session_state.conversationsDictionary.append(
            {"role": "assistant", "content": full_response})
