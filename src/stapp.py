import pandas as pd
import streamlit as st
from etl.transform.transform import list_IDs

df = pd.read_csv('data/output/trans_HoF.csv', encoding='ISO-8859-1')


def selector(df, player):
    try:
        return df[(df['playerID'] == player)]
    except Exception as e:
        print(f"An error occurred: {e}")


st.title('MLB Hall of Fame')

ID_list = list_IDs(df)

player = st.selectbox('Select a Hall of Famer', ID_list)

filtered_df = selector(df, player)
