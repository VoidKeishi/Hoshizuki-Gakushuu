def chatNihongo():
    import os
    import streamlit as st
    from openai import AzureOpenAI

    client = AzureOpenAI(
        api_key = st.secrets.API_KEY,  
        api_version = st.secrets.API_VERSION,
        azure_endpoint = st.secrets.END_POINT 
    )

    
    response = client.chat.completions.create(
        model="GPT35TURBO",  # model = "deployment_name".
        messages=st.session_state.conversationsChat
    )
    full_response = response.choices[0].message.content
    st.session_state.conversationsChat.append({"role": "assistant", "content": full_response})
