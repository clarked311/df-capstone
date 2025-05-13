import streamlit as st
from etl.load.load import load_HoF
from etl.transform.transform import transform_HoF
from etl.extract.extract import extract_HoF_data

st.title("MLB")

st.write("MLB Stats")


def etl_process():
    try:
        datasets = extract_HoF_data()

        HoF = datasets[1]
        People = datasets[0]
        Apps = datasets[2]

        trans_data = transform_HoF(HoF, People, Apps)

        load_HoF(trans_data)
    except Exception as e:
        print(f"An error occurred: {e}")
