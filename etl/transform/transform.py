import pandas as pd


def transform_HoF(HoF, People, Apps):
    try:
        People = column_manager(People)
        Apps = column_manager(Apps)
        ID_list = list_IDs(HoF)
        HoF = row_manager(HoF, ID_list)
        People = row_manager(People, ID_list)
        Apps = row_manager(Apps, ID_list)
        inter_data = HoF.merge(People, how='inner', copy=False)
        trans_data = inter_data.merge(Apps, how='inner', copy=False)
    except Exception as e:
        print(f"An error occurred: {e}")
    return trans_data


def column_manager(dataset):
    try:
        if 'deathCity' in dataset.columns:
            dataset.drop(['ID', 'bbrefID', 'retroID'], axis=1, inplace=True)
        elif 'G_all' in dataset.columns:
            col_to_drop = ['G_all', 'GS', 'G_batting', 'G_defense', 'G_p',
                           'G_c', 'G_1b', 'G_2b', 'G_3b', 'G_ss', 'G_lf',
                           'G_cf', 'G_rf', 'G_of', 'G_dh', 'G_ph', 'G_pr']
            dataset.drop(col_to_drop, axis=1, inplace=True)
        else:
            print('Dataset not found in manager')
    except Exception as e:
        print(f"An error occurred: {e}")
    return dataset


def list_IDs(dataset):
    try:
        ID_list = []
        mid_list = dataset.loc(dataset['inducted'] == 'Y', ['playerID'])
        ID_list = mid_list['playerID'].tolist()
    except Exception as e:
        print(f"An error occurred: {e}")
    return ID_list


def row_manager(dataset, ID_list):
    try:
        filtered_dataset = dataset.drop(not ID_list, axis=0, inplace=True)
    except Exception as e:
        print(f"An error occurred: {e}")
    return filtered_dataset
