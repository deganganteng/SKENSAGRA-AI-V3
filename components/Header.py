import components.subcomponents.Logo as Img
from components.subcomponents.Logo import *
import streamlit as st
import streamlit as st
def Header() :

    st.set_page_config(
        page_title="SKENSAGRA AI",
        page_icon="./Image/Logo_SMK.png",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    Img.image(["./Image/gema.png"])
    
    st.title("SKENSAGRA AI")
    st.write("Selamat datang di Pusat AI SMKN 1 GRATI kami siap membantu anda!")
    st.write("")