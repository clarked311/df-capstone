import streamlit as st
from etl.load.load import load_HoF_data
from etl.transform.transform import transform_HoF
from etl.extract.extract import extract_HoF

st.title("MLB")

st.write("MLB Stats")

datasets = load_HoF_data()

HoF = datasets[1]
People = datasets[0]
Apps = datasets[2]

trans_data = transform_HoF(HoF, People, Apps)

extract_HoF(trans_data)
