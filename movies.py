import pandas as pd
import streamlit as st

# Load the data
df = pd.read_csv('movies.csv')
df = df.dropna()

# Define the available titles
titles = list(df['Title'].unique())

# Define the Streamlit app
st.title('Top 200 Movies Info Outputer') # all streamlit features will be 'st'

selected_title = st.selectbox('Select a title', titles) # select the available regions

# below is the bulk of the app 
table = df.loc[df['Title'] == selected_title]
st.table(table)

