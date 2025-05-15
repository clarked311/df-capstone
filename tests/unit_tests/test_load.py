import pytest
import os
from etl.extract.extract import extract_HoF_data
from etl.transform.transform import transform_HoF
from etl.load.load import load_HoF


@pytest.fixture
def extracted_data():
    return extract_HoF_data()


def test_load_HoF(extracted_data):
    HoF = extracted_data[1]
    People = extracted_data[0]
    Apps = extracted_data[2]
    Teams = extracted_data[3]
    trans_data = transform_HoF(HoF, People, Apps, Teams)
    load_HoF(trans_data[0], trans_data[1], trans_data[2])
    assert (os.path.exists('data/output/trans_HoF.csv') is True)
