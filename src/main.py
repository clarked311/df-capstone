import streamlit as st
from etl.load.load import load_HoF
from etl.transform.transform import transform_HoF
from etl.extract.extract import extract_HoF_data

st.title("MLB")

st.write("MLB Stats")


def etl_process():
    try:
        dfs = extract_HoF_data()

        HoF = dfs[1]
        People = dfs[0]
        Apps = dfs[2]

        trans_data = transform_HoF(HoF, People, Apps)

        load_HoF(trans_data[0], trans_data[1], trans_data[2])
    except Exception as e:
        print(f"An error occurred: {e}")
