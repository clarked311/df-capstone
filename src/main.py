import pandas as pd
import streamlit as st
import plotly.express as px
from load import load_HoF_data
from transform import transform_HoF

st.title("MLB")

st.write("MLB Stats")

datasets = load_HoF_data()

HoF = datasets[1]
People = datasets[0]
Apps = datasets[2]

trans_data = transform_HoF(HoF, People, Apps)