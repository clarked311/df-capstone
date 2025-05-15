import pandas as pd


# function to read in all the raw data needed
def extract_HoF_data():

    try:
        # reading in each csv individually
        People = pd.read_csv('data/raw/People.csv', encoding='ISO-8859-15')
        HoF = pd.read_csv('data/raw/HallOfFame.csv', encoding='ISO-8859-15')
        Apps = pd.read_csv('data/raw/Appearances.csv', encoding='ISO-8859-15')
        Teams = pd.read_csv('data/raw/Teams.csv', encoding='ISO-8859-15')
    except Exception as e:
        print(f"An error occurred in extract_HoF_data: {e}")
    # returning the dataframes as a tuple
    return People, HoF, Apps, Teams
