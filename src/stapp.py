import pandas as pd
import streamlit as st
from etl.transform.transform import list_IDs

df = pd.read_csv('data/output/trans_HoF.csv', encoding='ISO-8859-1')


def selector(df, player):
    try:
        return df[(df['playerID'] == player)]
    except Exception as e:
        print(f"An error occurred in selector: {e}")


def display_name(opt):
    try:
        return ID_list[opt]
    except Exception as e:
        print(f"An error occurred in display_name: {e}")


def write_days(df):
    try:
        month_to_name = {
            '1': 'January',
            '2': 'February',
            '3': 'March',
            '4': 'April',
            '5': 'May',
            '6': 'June',
            '7': 'July',
            '8': 'August',
            '9': 'September',
            '10': 'October',
            '11': 'November',
            '12': 'December'
        }

        bm = str(int(df['birthMonth'].iloc[0]))
        bday = str(int(df['birthDay'].iloc[0])) + ' ' + month_to_name[bm] \
            + ' ' + str(int(df['birthYear'].iloc[0]))

        st.write('Born: ', bday)

        death = ''
        dd = df['deathDay'].iloc[0]
        dm = df['deathMonth'].iloc[0]
        dy = df['deathYear'].iloc[0]

        if pd.notna(dd) or pd.notna(dm) or pd.notna(dy):
            dds = ''
            dms = ''
            dys = ''
            if pd.notna(dd):
                dds = str(int(dd))
            if pd.notna(dm):
                dms = str(int(dm))
                dms = month_to_name[dms]
            if pd.notna(dy):
                dys = str(int(dy))
            death = dds + ' ' + dms + ' ' + dys
            
        st.write('Died: ', death)
    except Exception as e:
        print(f"An error occurred in write_days: {e}")



def play_info(df):
    try:
        pass
    except Exception as e:
        print(f"An error occurred in play_info: {e}")



st.title('MLB Hall of Fame')

ID_list = list_IDs(df)

player = st.selectbox('Select a Hall of Famer',
                      ID_list.keys(), format_func=display_name)

filtered_df = selector(df, player)

write_days(filtered_df)

filtered_df
