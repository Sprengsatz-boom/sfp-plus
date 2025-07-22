import streamlit as st

def set_background():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(-23deg, #ff512a, #5bffa6, #ffc67e, #ffa989);
            background-size: 500% 500%;
            animation: gradientBG 10s ease infinite;
        }

        @keyframes gradientBG {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background()