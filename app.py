import streamlit as st 

st.write("Hello World")

st.title("Streamlit Quick Demo")

st.header("This is a header")
st.subheader("This is a subheader")

st.text("This is some text.")
st.markdown("**This is some markdown text.**")

if st.button("Click me"):
    st.snow()
    st.write("Button clicked!")
