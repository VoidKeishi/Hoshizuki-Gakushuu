def dictionary():
    import streamlit as st
    from openai import AzureOpenAI

    client = AzureOpenAI(
        api_key="16ed8a71e992441f98be936d5767fea4",
        api_version="2023-05-15",
        # Your Azure OpenAI resource's endpoint value.
        azure_endpoint="https://sunhackathon22.openai.azure.com/"
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
            response = client.chat.completions.create(
                model="GPT35TURBO",  # model = "deployment_name".
                messages=st.session_state.conversationsDictionary
            )
            full_response = response.choices[0].message.content
            message_placeholder.markdown(full_response)
        st.session_state.conversationsDictionary.append(
            {"role": "assistant", "content": full_response})
