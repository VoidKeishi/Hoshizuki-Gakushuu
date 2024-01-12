import streamlit as st

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
    st.write("""
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    """)
    st.image("https://static.streamlit.io/examples/dice.jpg")
    if prompt := st.text_input("What's up bro ?"):
      with st.chat_message("user"):
          st.write(prompt)
          st.image("https://static.streamlit.io/examples/dice.jpg")
          st.image("https://static.streamlit.io/examples/dice.jpg")
          st.image("https://static.streamlit.io/examples/dice.jpg")