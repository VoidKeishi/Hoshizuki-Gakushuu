def chatNihongo():
    import os
    import streamlit as st
    from openai import AzureOpenAI

    client = AzureOpenAI(
        api_key = os.getenv("API_KEY"),  
        api_version = os.getenv("API_VERSION"),
        azure_endpoint = os.getenv("END_POINT")
    )

    
    response = client.chat.completions.create(
        model="GPT35TURBO",  # model = "deployment_name".
        messages=st.session_state.conversationsChat
    )
    full_response = response.choices[0].message.content
    st.session_state.conversationsChat.append({"role": "assistant", "content": full_response})
