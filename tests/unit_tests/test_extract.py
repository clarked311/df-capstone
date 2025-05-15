import pytest
from etl.extract.extract import extract_HoF_data


@pytest.fixture
def extracted_data():
    return extract_HoF_data()


def test_people_loaded(extracted_data):
    assert (
        'nameGiven' in extracted_data[0].columns
    ), 'nameGiven should be only in People'


def test_hof_loaded(extracted_data):
    assert (
        'votedBy' in extracted_data[1].columns
    ), 'votedBy should be only in HoF'


def test_apps_loaded(extracted_data):
    assert (
        'G_p' in extracted_data[2].columns
    ), 'G_p should be only in Apps'


def test_teams_loaded(extracted_data):
    assert (
        'franchID' in extracted_data[3].columns
    ), 'franchID should be only in Teams'
