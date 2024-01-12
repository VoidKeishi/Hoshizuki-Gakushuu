def makeQuiz():
    import streamlit as st
    from openai import AzureOpenAI

    print("Make Quiz feature is rendering...\n")

    client = AzureOpenAI(
        api_key="16ed8a71e992441f98be936d5767fea4",
        api_version="2023-05-15",
        # Your Azure OpenAI resource's endpoint value.
        azure_endpoint="https://sunhackathon22.openai.azure.com/"
    )

    content = "You are a brilliant teacher that teach Japanese. You love to give your student quizes of all JLPT Level. Beside that, you always provide them the detail explaination of the quiz"

    if "conversationsQuiz" not in st.session_state:
        st.session_state.conversationsQuiz = [
            {"role": "system", "content": content}]

    for conversation in st.session_state.conversationsQuiz:
        if conversation["role"] != "system":
            with st.chat_message(conversation["role"]):
                st.markdown(conversation["content"])

    print("Before: ")
    for conversation in st.session_state.conversationsQuiz:
        print(conversation["role"] + ": " + conversation["content"])
    print("\n")

    if prompt := st.chat_input("What is up?"):
        print("Updating session state in Make Quiz...\n")
        st.session_state.conversationsQuiz.append(
            {"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            for response in client.chat.completions.create(
                model="GPT35TURBO",  # model = "deployment_name".
                messages=st.session_state.conversationsQuiz,
                stream=True
            ):
                full_response += response.choices[0].delta.content or ""
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        st.session_state.conversationsQuiz.append(
            {"role": "assistant", "content": full_response})
    print("After: ")
    for conversation in st.session_state.conversationsQuiz:
        print(conversation["role"] + ": " + conversation["content"])
    print("\n")