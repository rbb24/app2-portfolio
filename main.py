import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ralf Binder")
    content = """
    Hi, 
    I am Ralf.
    I begin learning Python, to enhance my skills for administration IT infrastructure.
    Python will be handy especially for Ansible automation.
    But also like to automate other tasks in my company.
    """
    st.info(content)

content2 = """
Below you can find some of my apps I have built with Python. Feel free to contact me.
"""
st.write(content2)
