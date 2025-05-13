from pathlib import Path


def extract_HoF(dataset):
    try:
        filepath = Path('data/output/trans_HoF.csv')
        filepath.parent.mkdir(parents=True, exist_ok=True)
        dataset.to_csv(filepath)
    except Exception as e:
        print(f'An error occurred: {e}')
    return 'Extracted'
