import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Elisa Cabañas")
    content = """
    Hi I am Elisa C. ....dadiuhiduauidhaudhaidaiduhiuad
    """
    st.info(content)

st.write("Below you can find some of the apps I have built in Python. Feel free to contact me!")
