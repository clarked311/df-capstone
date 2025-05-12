import pandas as pd
import streamlit as st
import plotly.express as px
from load.py import load_HoF_data

st.title("MLB")

st.write("MLB Stats")

datasets = load_HoF_data()

HoF = datasets[1]
people = datasets[0]