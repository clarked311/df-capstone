import pytest
import pandas as pd
from src.stapp import selector, display_name, name_picker, write_days, \
    play_info, HoF_tracker, team_chart


@pytest.fixture
def b_data():
    HoF = pd.read_csv('data/output/trans_HoF.csv', encoding='ISO-8859-1')
    People = pd.read_csv('data/output/trans_People.csv', encoding='ISO-8859-1')
    Apps = pd.read_csv('data/output/trans_Apps.csv', encoding='ISO-8859-1')
    return HoF, People, Apps


def test_selector(b_data):
    HoF = b_data[0]
    t_df = selector(HoF, 'beltrad01')
    assert (t_df['yearid'].iloc[0] == 2024), 'Beltre inducted 2024'


def test_display_name(b_data):
    pass


def test_name_picker(b_data):
    pass


def test_write_days(b_data):
    pass


def test_play_info(b_data):
    pass


def test_HoF_tracker(b_data):
    pass


def test_team_chart(b_data):
    pass
