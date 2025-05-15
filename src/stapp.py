import pandas as pd
import streamlit as st
import plotly.express as px


# a function to reduce the df to the section containing the player
def selector(df, player):
    try:
        # making it so the only rows included have the correct playerID
        return df[(df['playerID'] == player)]
    except Exception as e:
        print(f"An error occurred in selector: {e}")


# a function to display the name of the player
def display_name(opt):
    try:
        # just returning the correct part of the list
        return ID_list[opt]
    except Exception as e:
        print(f"An error occurred in display_name: {e}")


# a function to allow picking a name of a player
def name_picker(df):
    try:
        # initialising empty ID_list
        ID_list = {}
    except Exception as e:
        print(f"An error occurred in ID_list setup: {e}")
    try:
        # specifying which columns to keep
        cols_to_ret = ['playerID', 'nameFirst', 'nameLast']
        # keeping those columns
        mid_list = df.loc[:, cols_to_ret]
    except Exception as e:
        print(f"An error occurred in mid_list: {e}")
    try:
        # creating a new variable with the player's full name
        name = mid_list['nameFirst'] + ' ' + mid_list['nameLast']
        # loading names in to dict with the ID as the key
        ID_list = pd.Series(name.to_numpy(),
                            index=mid_list['playerID']).to_dict()
    except Exception as e:
        print(f"An error occurred in ID_list allocation: {e}")
    # returning the dictionary
    return ID_list


# a function to write the birth and death days
def write_days(df):
    try:
        # a dictionary of month names
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

        # obtaining the birth month
        bm = str(int(df['birthMonth'].iloc[0]))
        # creating a string to list out the birthday in a nice format
        bday = str(int(df['birthDay'].iloc[0])) + ' ' + month_to_name[bm] \
            + ' ' + str(int(df['birthYear'].iloc[0]))

        # writing the string
        st.write('Born: ', bday)

        # initialising death string
        death = ''
        # obtaining the values of death
        dd = df['deathDay'].iloc[0]
        dm = df['deathMonth'].iloc[0]
        dy = df['deathYear'].iloc[0]

        # only running if the person is dead
        # not all people have all parts of their death present
        if pd.notna(dd) or pd.notna(dm) or pd.notna(dy):
            # initialising strings
            dds = ''
            dms = ''
            dys = ''
            # if there is a death day, writing that
            if pd.notna(dd):
                dds = str(int(dd))
            # if there is a death day, writing that
            if pd.notna(dm):
                dms = str(int(dm))
                # converting the death month to a string
                dms = month_to_name[dms]
            # if there is a death day, writing that
            if pd.notna(dy):
                dys = str(int(dy))
            # adding strings to death
            death = dds + ' ' + dms + ' ' + dys

        # writing death date if it's there and leaving it blank otherwise
        st.write('Died: ', death)
    except Exception as e:
        print(f"An error occurred in write_days: {e}")


# a function to write the players biographical info
def play_info(df):
    try:
        # initialising the columns to write the metrics to
        col1, col2 = st.columns(2)

        # setting up the left-hand side
        with col1:
            # writing metrics with their appropriate label and value
            st.metric(label='Height', value=f'{int(df['height'].iloc[0])}in')
            st.metric(label='Throws', value=f'{df['throws'].iloc[0]}')
            st.metric(label='Debut', value=f'{df['debut'].iloc[0]}')
        # doing the same for corresponding right-hand metrics
        with col2:
            st.metric(label='Weight', value=f'{int(df['weight'].iloc[0])}lbs')
            st.metric(label='Bats', value=f'{df['bats'].iloc[0]}')
            st.metric(label='Final Game', value=f'{df['finalGame'].iloc[0]}')

    except Exception as e:
        print(f"An error occurred in play_info: {e}")


# a function to generate graphs to show the voting process
def HoF_tracker(df):
    try:
        # same columns as above
        col1, col2 = st.columns(2)
        # making year an integer
        df['yearid'] = df['yearid'].apply(lambda year: f"{year}")
        # on your left
        with col1:
            # a chart to show the votes and amount needed over the years
            st.line_chart(data=df, x='yearid', y=['needed', 'votes'],
                          x_label='year', y_label='votes',
                          color=['#000000', '#0000FF'])
        # on your right
        with col2:
            # a chart showing vote share over the years
            st.line_chart(data=df, x='yearid', y=['vote_share'],
                          x_label='year', y_label='vote %',
                          color='#0000FF')
    except Exception as e:
        print(f"An error occurred in HoF_tracker: {e}")


# a function to traw a team chart
def team_chart(df):
    try:
        # paring down the df to only name and yearID
        filtered_df = df.loc[:, ['name', 'yearID']]
        # renaming yearID to x_start for consistency
        filtered_df = filtered_df.rename(columns={'yearID': 'x_start'})
        # in this, the end year is the same as the start
        filtered_df['x_end'] = filtered_df.loc[:, ['x_start']]
        # applying -01-01 to the start of the year
        filtered_df['x_start'] = \
            filtered_df['x_start'].apply(lambda year: f"{year}-01-01")
        # applying -12-31 to the end of the year
        filtered_df['x_end'] = \
            filtered_df['x_end'].apply(lambda year: f"{year}-12-31")

        # making a plotly.express timeline of teams
        fig = px.timeline(filtered_df, x_start="x_start", x_end="x_end",
                          y="name", color_discrete_sequence=["tan"])

        # writing the chart to streamlit
        st.plotly_chart(fig)
    except Exception as e:
        print(f"An error occurred in team_chart: {e}")


# the execution starts here
# reading in the transformed data
HoF = pd.read_csv('data/output/trans_HoF.csv', encoding='ISO-8859-1')
People = pd.read_csv('data/output/trans_People.csv', encoding='ISO-8859-1')
Apps = pd.read_csv('data/output/trans_Apps.csv', encoding='ISO-8859-1')

# adding a nice title
st.title('MLB Hall of Fame')

# grabbing the ID_list
ID_list = name_picker(People)

# allowing the user to select a person
player = st.selectbox('Select a Hall of Famer',
                      ID_list.keys(), format_func=display_name)

# filtering the dfs with the selected player
filtered_HoF = selector(HoF, player)
filtered_People = selector(People, player)
filtered_Apps = selector(Apps, player)

# writing the birth and death days
write_days(filtered_People)

# writing the player biographical info
play_info(filtered_People)

# generating the HoF charts
HoF_tracker(filtered_HoF)

# generating the team chart
team_chart(filtered_Apps)
