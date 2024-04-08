import streamlit as st
st.title("This is my first streamlit project")
st.write("Hello Streamlit!")
st.write("Hello Streamlit!")
st.write("one more thing")
st.title("And one more title")
st.header("This is the header")
st.latex(r'''a + ar^1''')

st.checkbox('yes')
st.button('Click')
st.radio('Pick you gender', ['Male', 'Female'])
st.selectbox('Pick your gender', ['Male', 'Gender'])
st.multiselect('choose a planet', ['Jupiter', 'Mars', 'Neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0.50)

st.checkbox('yes')