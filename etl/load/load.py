import pandas as pd

try:
    People = pd.read_csv('data/raw/People.csv')
    HoF = pd.read_csv('data/raw/HallOfFame.csv')
except Exception as e:
    print(f"An error occurred: {e}")
