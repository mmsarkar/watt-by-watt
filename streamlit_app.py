import streamlit as st

st.title("Watt by Watt")
st.write("Select your town for more stats!")

button1 = st.button("Los Angeles")
if(button1):
  sf.write("You are from LA!")
  
button2 = st.button("Irvine")
if(button2):
  sf.write("You are from Irvine!")
  
button3 = st.button("Riverside")
if(button3):
  sf.write("You are from Riverside!")

