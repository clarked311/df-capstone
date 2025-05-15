from pathlib import Path


# a function to load the transformed data in to the endpoint
def load_HoF(HoF, People, Apps):
    try:
        # the filepath variables tell pd where to write
        filepath = Path('data/output/trans_HoF.csv')
        # .to_csv writes the file to the specified location.
        # the encoding is there to avoid corruption.
        HoF.to_csv(filepath, encoding='ISO-8859-1')
        filepath = Path('data/output/trans_People.csv')
        People.to_csv(filepath, encoding='ISO-8859-1')
        filepath = Path('data/output/trans_Apps.csv')
        Apps.to_csv(filepath, encoding='ISO-8859-1')
    except Exception as e:
        print(f'An error occurred in load_HoF: {e}')
    return 'Extracted'
