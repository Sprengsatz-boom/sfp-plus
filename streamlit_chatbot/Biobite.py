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
         @keyframes fall {
            0% {
                top: -50px;
                opacity: 1;
                transform: translateX(0) rotate(0deg);
            }
            100% {
                top: 110vh;
                opacity: 0.6;
                transform: translateX(100px) rotate(360deg);
            }
        }

        .falling-fruit {
            position: absolute;
            width: 40px;
            top: -50px;
            z-index: 0;
            animation-name: fall;
            animation-timing-function: linear;
            animation-iteration-count: infinite;
        }

        .fruit-1 { left: 10%; animation-duration: 6s; animation-delay: 0s; }
        .fruit-2 { left: 30%; animation-duration: 8s; animation-delay: 1s; }
        .fruit-3 { left: 50%; animation-duration: 5s; animation-delay: 2s; }
        .fruit-4 { left: 70%; animation-duration: 7s; animation-delay: 3s; }
        .fruit-5 { left: 90%; animation-duration: 9s; animation-delay: 4s; }
        </style>

        <!-- Fruit images placed absolutely -->
        <img class="falling-fruit fruit-1" src="https://cdn-icons-png.flaticon.com/512/590/590685.png" />
        <img class="falling-fruit fruit-2" src="https://cdn-icons-png.flaticon.com/128/25/25345.png" />
        <img class="falling-fruit fruit-3" src="https://cdn-icons-png.flaticon.com/512/590/590707.png" />
        <img class="falling-fruit fruit-4" src="https://cdn-icons-png.flaticon.com/128/765/765608.png" />
        <img class="falling-fruit fruit-5" src="https://cdn-icons-png.flaticon.com/512/590/590692.png" />
        """,
        unsafe_allow_html=True
    )

set_background()

mute = st.checkbox("Mute Background Music", value=True)

video_id = "gpBLrDBmHts"
autoplay = 1
loop = 1
playlist = video_id  # required for looping single video
mute_param = 1 if mute else 0

iframe = f"""
<iframe
    width="0"
    height="0"
    src="https://www.youtube.com/embed/{video_id}?autoplay={autoplay}&loop={loop}&playlist={playlist}&mute={mute_param}&controls=0&modestbranding=1&iv_load_policy=3&rel=0"
    frameborder="0"
    allow="autoplay; encrypted-media"
    allowfullscreen
></iframe>
"""

st.markdown(iframe, unsafe_allow_html=True)

st.write("Toggle mute on/off to control the background music.")