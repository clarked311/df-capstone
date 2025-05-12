import pandas as pd


def transform_HoF(HoF, People, Apps):
    try:
        column_manager(People)
        column_manager(Apps)
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
