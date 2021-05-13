import streamlit as st
import numpy as np
from load_css import local_css

local_css("style.css")


st.markdown('**Markdown**') 
option = st.sidebar.selectbox(
    'Which number do you like best?',
     'arf')


st.title("Hello GeeksForGeeks !!!")


# Header
st.header("This is a header") 
  
# Subheader
st.subheader("This is a subheader")

# Text
st.text("Hello GeeksForGeeks!!!")

# Markdown
st.markdown("### This is a markdown")

# success
st.success("Success")

# success
st.info("Information")

# success
st.warning("Warning")

# success
st.error("Error")

# Write text
st.write("Text with write")

# Writing python inbuilt function range()
st.write(range(10))

# checkbox
# check if the checkbox is checked
# title of the checkbox is 'Show/Hide'
if st.checkbox("Show/Hide"):
        
    # dispaly the text if the checkbox returns True value
    st.text("Showing the widget")

# Create a simple button that does nothing
st.button("Click me for no reason")

# Create a button, that when clicked, shows a text
if(st.button("About")):
	st.text("Welcome To GeeksForGeeks!!!")


# Text Input

# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area
name = st.text_input("Enter Your name", "Type Here ...")

# display the name when the submit button is clicked
# .title() is used to get the input text string
if(st.button('Submit')):
	result = name.title()
	st.success(name)

st.info("Prediction dependency: 80%")

st.info("This BERT model was trained on YELP Reviews using PyTorch")

# st.write('<style>{<font color=‘red’>THIS TEXT WILL BE RED</font>}</style>, unsafe_allow_html=True')

t = "<div>Hello there my <span class='highlight blue'>name <span class='bold'>yo</span> </span> is <span class='highlight red'>Fanilo <span class='bold'>Name</span></span></div>"
st.markdown(t, unsafe_allow_html=True)