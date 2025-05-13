from pathlib import Path


def load_HoF(df):
    try:
        filepath = Path('data/output/trans_HoF.csv')
        df.to_csv(filepath, encoding='ISO-8859-1')
    except Exception as e:
        print(f'An error occurred: {e}')
    return 'Extracted'
