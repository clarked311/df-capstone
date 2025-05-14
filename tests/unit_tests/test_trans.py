import pytest
from etl.extract.extract import extract_HoF_data
from etl.transform.transform import transform_HoF, column_manager, \
 list_IDs, row_manager


@pytest.fixture
def extracted_data():
    return extract_HoF_data()


def test_ID_list(extracted_data):
    ID_list = list_IDs(extracted_data[1])
    assert ('aaronha01' in ID_list), 'Hank Aaron made the HoF'
    assert ('abbotji01' not in ID_list), 'Jim Abbot did not enter HoF'


def test_column_manager(extracted_data):
    People = column_manager(extracted_data[0])
    assert ('debut' in People.columns), 'debut date should remain'
    assert ('bbrefID' not in People.columns), 'bbrefID has been dropped'
    Apps = column_manager(extracted_data[2])
    assert ('lgID' in Apps.columns), 'lgID should remain'
    assert ('G_p' not in Apps.columns), 'G_p has been dropped'
    Teams = column_manager(extracted_data[3])
    assert ('name' in Teams.columns), 'name should remain'
    assert ('BPF' not in Teams.columns), 'BPF has been dropped'


def test_row_manager(extracted_data):
    ID_list = list_IDs(extracted_data[1])
    People = extracted_data[0]
    peop_test = row_manager(People, ID_list)
    assert (peop_test['playerID'].iloc[0] == 'aaronha01'), 'Hank Aaron #1'
    assert ('biggica01' not in peop_test['playerID']), 'Cavan still active'


def test_transform_HoF(extracted_data):
    HoF = extracted_data[1]
    People = extracted_data[0]
    Apps = extracted_data[2]
    Teams = extracted_data[3]
    data = transform_HoF(HoF, People, Apps, Teams)
    HoF = data[0]
    People = data[1]
    Apps = data[2]
    assert ('debut' in People.columns), 'debut date should remain'
    assert ('bbrefID' not in People.columns), 'bbrefID has been dropped'
    assert (HoF['playerID'].iloc[0] == 'aaronha01'), 'Hank Aaron #1'
    assert ('biggica01' not in HoF['playerID']), 'Cavan still active'
    assert ('name' in Apps.columns), 'testing the merged columns'
    assert (Apps['franchID'].iloc[0] == 'BNA'), 'Merged data'
