import pytest
import pandas as pd
import tests.data_processing as data_processing 

def test_load_data_valid_file():
    df = data_processing.load_data("vgsales_cleaned.csv")
    assert isinstance(df, pd.DataFrame)

def test_load_data_invalid_file():
    with pytest.raises(FileNotFoundError):
        data_processing.load_data("invalid_file.csv")