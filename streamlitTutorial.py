import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello GPT")
name = st.text_input("Ask your questions")

st.write("This is your first streamlit app")

st.text("let's get started")

name = st.text_input("Enter your name")
if st.button("Greet"):
    st.success(f"Hello, {name}")

# How to upload csv file
upload_file = st.file_uploader("upload a csv", type='csv')
if upload_file:
    df = pd.read_csv(upload_file)
    st.dataframe(df)

st.header("This is heeader")
st.subheader("This is a subheader")
st.markdown("[Link](https://streamlit.io/)")
st.text_area("write your message")
st.number_input('pick a number', min_value=0, max_value=10)
st.slider("Choose a range",0,100)
st.selectbox("select a fruit",["apple","banana","mango"])
st.multiselect("select language",["java","python","c","c++"])
st.radio("pick one",["option A","option B"])
st.checkbox("I agree terms & conditions")

if st.checkbox("show details"):
    st.info("here are more details")

# form tag
with st.form("login form"):
    username = st.text_input("Enter username")
    password = st.text_input("password", type="password")
    submitted = st.form_submit_button("Login")

    if submitted:
        st.success(f"wlecome,{username}")

df = pd.DataFrame(np.random.randn(20,3),columns = ["A","B","C"])
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

st.video("https://www.youtube.com/watch?v=MLtkcIBUmQk")
st.image("https://imgs.search.brave.com/vhxh6_OrgT4gYk91bxGWW_3wQjXX5RRSYZ3j6pYBPuo/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9pLnBp/bmltZy5jb20vb3Jp/Z2luYWxzLzg2LzFh/LzVkLzg2MWE1ZDU4/ZTY1ZTk0MTliNDAx/NzU3MDRiM2NhOTAz/LmpwZw",caption="sample image")