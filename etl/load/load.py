import pandas as pd

try:
    HoF = pd.read_csv('data/raw/HallOfFame.csv')

    print(HoF)
except Exception as e:
    print(f"An error occurred: {e}")
