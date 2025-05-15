import pytest
import os
import pandas as pd
from src.main import etl_process


@pytest.fixture
def ran_etl():
    return etl_process()


def test_etl_process(ran_etl):
    assert (os.path.exists('data/output/trans_HoF.csv') is True)
    HoF = pd.read_csv('data/output/trans_HoF.csv', encoding='ISO-8859-1')
    assert ('yearid' in HoF.columns), 'checking columns'
    assert (HoF['yearid'].iloc[0] == 1982), 'checking data'
    Apps = pd.read_csv('data/output/trans_Apps.csv', encoding='ISO-8859-1')
    assert ('lgID_x' in Apps.columns), 'checking merge'
    assert ('SB' not in Apps.columns), 'checking drop'
    assert (Apps['franchID'].iloc[0] == 'BNA'), 'checking data'
