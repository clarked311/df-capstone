import pandas as pd
import streamlit as st
import plotly.express as px


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


def name_picker(df):
    try:
        ID_list = []
    except Exception as e:
        print(f"An error occurred in ID_list setup: {e}")
    try:
        cols_to_ret = ['playerID', 'nameFirst', 'nameLast']
        mid_list = df.loc[:, cols_to_ret]
    except Exception as e:
        print(f"An error occurred in mid_list: {e}")
    try:
        name = mid_list['nameFirst'] + ' ' + mid_list['nameLast']
        ID_list = pd.Series(name.to_numpy(),
                            index=mid_list['playerID']).to_dict()
    except Exception as e:
        print(f"An error occurred in ID_list allocation: {e}")
    return ID_list


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
        col1, col2 = st.columns(2)

        with col1:
            st.metric(label='Height', value=f'{int(df['height'].iloc[0])}in')
            st.metric(label='Throws', value=f'{df['throws'].iloc[0]}')
            st.metric(label='Debut', value=f'{df['debut'].iloc[0]}')
        with col2:
            st.metric(label='Weight', value=f'{int(df['weight'].iloc[0])}lbs')
            st.metric(label='Bats', value=f'{df['bats'].iloc[0]}')
            st.metric(label='Final Game', value=f'{df['finalGame'].iloc[0]}')

    except Exception as e:
        print(f"An error occurred in play_info: {e}")


def HoF_tracker(df):
    try:
        col1, col2 = st.columns(2)
        df['yearid'] = df['yearid'].apply(lambda year: f"{year}")
        with col1:
            st.line_chart(data=df, x='yearid', y=['needed', 'votes'],
                        x_label='year', y_label='votes',
                        color=['#000000', '#0000FF'])
        with col2:
            st.line_chart(data=df, x='yearid', y=['vote_share'],
                        x_label='year', y_label='vote %',
                        color='#0000FF')
    except Exception as e:
        print(f"An error occurred in HoF_tracker: {e}")


def team_chart(df):
    try:
        filtered_df = df.loc[:, ['name', 'yearID']]
        filtered_df = filtered_df.rename(columns={'yearID': 'x_start'})
        filtered_df['x_end'] = filtered_df.loc[:, ['x_start']]
        filtered_df['x_start'] = \
            filtered_df['x_start'].apply(lambda year: f"{year}-01-01")
        filtered_df['x_end'] = \
            filtered_df['x_end'].apply(lambda year: f"{year}-12-31")

        fig = px.timeline(filtered_df, x_start="x_start", x_end="x_end",
                          y="name", color_discrete_sequence=["tan"])

        st.plotly_chart(fig)
    except Exception as e:
        print(f"An error occurred in team_chart: {e}")


HoF = pd.read_csv('data/output/trans_HoF.csv', encoding='ISO-8859-1')
People = pd.read_csv('data/output/trans_People.csv', encoding='ISO-8859-1')
Apps = pd.read_csv('data/output/trans_Apps.csv', encoding='ISO-8859-1')

st.title('MLB Hall of Fame')

ID_list = name_picker(People)

player = st.selectbox('Select a Hall of Famer',
                      ID_list.keys(), format_func=display_name)

filtered_HoF = selector(HoF, player)
filtered_People = selector(People, player)
filtered_Apps = selector(Apps, player)

write_days(filtered_People)

play_info(filtered_People)

HoF_tracker(filtered_HoF)

team_chart(filtered_Apps)

filtered_Apps

filtered_HoF
