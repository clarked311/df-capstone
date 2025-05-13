import pandas as pd


def extract_HoF_data():

    try:
        People = pd.read_csv('data/raw/People.csv', engine='python')
        HoF = pd.read_csv('data/raw/HallOfFame.csv', engine='python')
        Apps = pd.read_csv('data/raw/Appearances.csv', engine='python')
    except Exception as e:
        print(f"An error occurred: {e}")
    return People, HoF, Apps
