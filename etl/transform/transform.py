import pandas as pd

def transform_HoF(HoF, People):
    try:
        column_manager(HoF)
        column_manager(People)
    except Exception as e:
        print(f"An error occurred: {e}")
    return trans_data

def column_manager(dataset):
    try:
        if 'inducted' in dataset.columns:
            dataset
        elif 'deathCity' in dataset.columns:
            dataset.drop('retroID', axis=1, inplace=True)
    except Exception as e:
        print(f"An error occurred: {e}")
    return dataset
