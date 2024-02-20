import streamlit as st
import pandas as pd

st.title("This is a title")
st.header("This is a header")
st.markdown("*italic*")

df = pd.read_csv("train.csv")
st.dataframe(df)
