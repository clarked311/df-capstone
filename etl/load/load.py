from pathlib import Path


def load_HoF(HoF, People, Apps, Teams):
    try:
        filepath = Path('data/output/trans_HoF.csv')
        HoF.to_csv(filepath, encoding='ISO-8859-1')
        filepath = Path('data/output/trans_People.csv')
        People.to_csv(filepath, encoding='ISO-8859-1')
        filepath = Path('data/output/trans_Apps.csv')
        Apps.to_csv(filepath, encoding='ISO-8859-1')
        filepath = Path('data/output/trans_Teams.csv')
        Teams.to_csv(filepath, encoding='ISO-8859-1')
    except Exception as e:
        print(f'An error occurred in load_HoF: {e}')
    return 'Extracted'
