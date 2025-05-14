import pandas as pd


def transform_HoF(HoF, People, Apps):
    try:
        People = column_manager(People)
        Apps = column_manager(Apps)
        ID_list = list_IDs(HoF)
        HoF = row_manager(HoF, ID_list)
        People = row_manager(People, ID_list)
        Apps = row_manager(Apps, ID_list)
    except Exception as e:
        print(f"An error occurred in transform_HoF: {e}")
    return HoF, People, Apps


def column_manager(df):
    try:
        if 'deathCity' in df.columns:
            df.drop(['ID', 'bbrefID', 'retroID'], axis=1, inplace=True)
        elif 'G_all' in df.columns:
            col_to_drop = ['G_all', 'GS', 'G_batting', 'G_defense', 'G_p',
                           'G_c', 'G_1b', 'G_2b', 'G_3b', 'G_ss', 'G_lf',
                           'G_cf', 'G_rf', 'G_of', 'G_dh', 'G_ph', 'G_pr']
            df.drop(col_to_drop, axis=1, inplace=True)
        else:
            print('df not found in manager')
    except Exception as e:
        print(f"An error occurred in column_manager: {e}")
    return df


def list_IDs(df):
    try:
        ID_list = []
    except Exception as e:
        print(f"An error occurred in ID_list setup: {e}")
    try:
        cols_to_ret = ['playerID', 'nameFirst', 'nameLast']
        mid_list = df.loc[df['inducted'] == 'Y', cols_to_ret]
    except Exception as e:
        print(f"An error occurred in mid_list: {e}")
    try:
        name = mid_list['nameFirst'] + ' ' + mid_list['nameLast']
        ID_list = pd.Series(name.to_numpy(),
                            index=mid_list['playerID']).to_dict()
    except Exception as e:
        print(f"An error occurred in ID_list allocation: {e}")
    return ID_list


def row_manager(df, ID_list):
    try:
        filtered_df = df[df['playerID'].isin(ID_list)]
    except Exception as e:
        print(f"An error occurred in row_manager: {e}")
    return filtered_df
