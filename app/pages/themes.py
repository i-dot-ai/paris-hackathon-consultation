import streamlit as st
import pandas as pd
import os



def themed_data():
    responses_df = pd.read_json("example_data/outputs/mappings_nuclear_plant.json")
    st.write(responses_df)
    responses_df = responses_df.explode(["reasons", "labels", "stances"])
    return responses_df


st.title("Here are the themes from your data")
st.write("hi")
# st.write(themed_data())
st.write(os.getcwd())
st.write(os.listdir())
st.write(themed_data())


