import pandas as pd


# the overarching function to transform the data
def transform_HoF(HoF, People, Apps, Teams):
    try:
        # sending the dfs with columns to be dropped to the manager
        People = column_manager(People)
        Apps = column_manager(Apps)
        Teams = column_manager(Teams)
        # getting the ID list
        ID_list = list_IDs(HoF)
        # paring down the dfs to those with required IDs
        HoF = row_manager(HoF, ID_list)
        People = row_manager(People, ID_list)
        Apps = row_manager(Apps, ID_list)
        # added vote share to the HoF table
        HoF = vpc(HoF)
        # merged teams on to the appearances table
        # so the appearances have the name attached
        Apps = pd.merge(Apps, Teams, 'inner', on=['teamID', 'yearID'])
    except Exception as e:
        print(f"An error occurred in transform_HoF: {e}")
    # returned the transformed dfs as a tuple
    return HoF, People, Apps


# a function to drop columns that are unnecessary
def column_manager(df):
    try:
        # deathCity is only in people, so that identifies it
        if 'deathCity' in df.columns:
            # dropping the 3 columns i don't want
            df.drop(['ID', 'bbrefID', 'retroID'], axis=1, inplace=True)
        # g_all is only in apps
        elif 'G_all' in df.columns:
            # col_to_drop made for readability
            col_to_drop = ['G_all', 'GS', 'G_batting', 'G_defense', 'G_p',
                           'G_c', 'G_1b', 'G_2b', 'G_3b', 'G_ss', 'G_lf',
                           'G_cf', 'G_rf', 'G_of', 'G_dh', 'G_ph', 'G_pr']
            # dropping the columns stated above
            df.drop(col_to_drop, axis=1, inplace=True)
        # attendance is only in teams
        elif 'attendance' in df.columns:
            # col_to_drop made for readability
            col_to_drop = ['divID', 'Rank', 'G', 'Ghome', 'W', 'L',
                           'DivWin', 'WCWin', 'LgWin', 'WSWin', 'R', 'AB',
                           'H', '2B', '3B', 'HR', 'BB', 'SO', 'SB', 'CS',
                           'HBP', 'SF', 'RA', 'ER', 'ERA', 'CG', 'SHO', 'SV',
                           'IPouts', 'HA', 'HRA', 'BBA', 'SOA', 'E', 'DP',
                           'FP', 'park', 'attendance', 'BPF', 'PPF',
                           'teamIDBR', 'teamIDlahman45', 'teamIDretro']
            # dropping the columns stated above
            df.drop(col_to_drop, axis=1, inplace=True)
            # removed the duplicate rows
            df.drop_duplicates(inplace=True)
        # printing to console if there is no column to drop
        else:
            print('df not found in manager')
    except Exception as e:
        print(f"An error occurred in column_manager: {e}")
    # returning the curtailed df
    return df


# a function to get the IDs of only the players who made the hall of fame
def list_IDs(df):
    try:
        # initialising ID_list as a list
        ID_list = []
    except Exception as e:
        print(f"An error occurred in ID_list setup: {e}")
    try:
        # creating a temporary df which just has the player IDs of those HoFers
        mid_list = df.loc[df['inducted'] == 'Y', ['playerID']]
    except Exception as e:
        print(f"An error occurred in mid_list: {e}")
    try:
        # converting it to a list for use later
        ID_list = mid_list['playerID'].tolist()
    except Exception as e:
        print(f"An error occurred in ID_list allocation: {e}")
    # returning the list
    return ID_list


# this is a function to reduce a df down to only the necessary rows
def row_manager(df, ID_list):
    try:
        # checks whether a row is in the id list
        # includes it in the dataframe if so
        filtered_df = df[df['playerID'].isin(ID_list)]
    except Exception as e:
        print(f"An error occurred in row_manager: {e}")
    # returns the newly filtered dataframe
    return filtered_df


# a function to calculate the vote percentage
def vpc(df):
    try:
        # creating a calculated column with the new data
        df['vote_share'] = (df['votes'] / df['ballots'])
    except Exception as e:
        print(f"An error occurred in vpc: {e}")
    # returning the new column to be added
    return df
