import pandas as pd


def transform_HoF(HoF, People, Apps):
    try:
        column_manager(People)
        column_manager(Apps)
        row_manager(HoF)
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
            col_to_drop = ['G_all', 'GS', 'G_batting', 'G_defense', 'G_p', 'G_c', 'G_1b', 'G_2b', 'G_3b', 'G_ss', 'G_lf', 'G_cf', 'G_rf', 'G_of', 'G_dh', 'G_ph', 'G_pr']
            dataset.drop(col_to_drop, axis=1, inplace=True)
        else:
            print('Dataset not found in manager')
    except Exception as e:
        print(f"An error occurred: {e}")
    return dataset


def row_manager(dataset):
    try:
        ID_list = list_IDs(dataset)
        managed_dataset = filter_rows(dataset, ID_list)
    except Exception as e:
        print(f"An error occurred: {e}")
    return managed_dataset


def list_IDs(dataset):
    try:
        ID_list = []
        mid_list = dataset.loc(dataset['inducted'] == 'Y', ['playerID'])
        ID_list = mid_list['playerID'].tolist()
    except Exception as e:
        print(f"An error occurred: {e}")
    return ID_list


def filter_rows(dataset, ID_list):
    try:
        filtered_dataset = []
    except Exception as e:
        print(f"An error occurred: {e}")
    return filtered_dataset
