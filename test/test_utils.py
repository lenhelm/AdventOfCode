from advent.year_2021.utils import get_data_path


def test_get_data_path():
    path = get_data_path()
    assert path.exists
