import streamlit as st

st.title("Welcome to Classification Page")
st.markdown("")
st.markdown("")

col1,col2 = st.columns(2)
#col1.header("Tomato")
col1.image("tomatoFinal.jpg",caption="Tomato")
#col2.header("Potato")
col2.image("potato.png",caption="Potato")

st.markdown("")
col3,col4 = st.columns(2)
#col3.header("Pepper Bell")
col3.image("Pepper.png",caption="Pepper Bell")
#col4.header("Cotton")
col4.image("cotton.png",caption="Cotton")


