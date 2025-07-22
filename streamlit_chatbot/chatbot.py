

import streamlit as st
import pandas as pd

st.title("BioBites")
st.header("Welcome to Dashboard")
st.write("this is a simple demonstration of streamlit capabilities")

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def main():
    st.title("The Chatbot")

    initialize_session_state()

    for message in st.session_state.messages:
        with st.chat_message(message["Role"]):
            st.write(message["content"])

    if prompt := st.chat_input("What's on your mind?"):
        with st.chat_message("user"):
            st.write(prompt)

        st.session_state.messages.append({"Role": "user", "content": prompt})

        response = f"You said: {prompt}"
        with st.chat_message("assistant"):
            st.write(response)

        st.session_state.messages.append({"Role": "assistant", "content": response})

if __name__ == "__main__":
    main()


df = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'January'],
    'Price': [1000, 1500, 2000, 1200]
})

st.sidebar.header("Filters")

selected_month = st.sidebar.selectbox(
    "Select Month",
    options=df['Month'].unique() 
)

price_range = st.sidebar.slider(
    "Select Price Range",
    min_value=0,
    max_value=3000,
    value=(0, 3000)
)