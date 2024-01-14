def chatNihongo():
    import streamlit as st
    from openai import AzureOpenAI

    client = AzureOpenAI(
        api_key="16ed8a71e992441f98be936d5767fea4",
        api_version="2023-05-15",
        # Your Azure OpenAI resource's endpoint value.
        azure_endpoint="https://sunhackathon22.openai.azure.com/"
    )
    
    response = client.chat.completions.create(
        model="GPT35TURBO",  # model = "deployment_name".
        messages=st.session_state.conversationsChat
    )
    full_response = response.choices[0].message.content
    st.session_state.conversationsChat.append({"role": "assistant", "content": full_response})
