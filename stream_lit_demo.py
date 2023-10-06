import streamlit as st

st.title("welcome to streamlit")

agree = st.checkbox('I agree')

if agree:
    st.write('Great!')

genere = st.radio("select genere",["a","b"],captions=["its a ","its not a"])


if genere == 'a':
    st.write('You selected comedy.')
else:
    st.write("You didn\'t select comedy.")