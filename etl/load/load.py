from pathlib import Path


def load_HoF(dataset):
    try:
        filepath = Path('data/output/trans_HoF.csv')
        dataset.to_csv(filepath)
    except Exception as e:
        print(f'An error occurred: {e}')
    return 'Extracted'
