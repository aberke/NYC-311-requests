""" TODO
"""

from datetime import (
    datetime,
    timedelta,
)


import pandas as pd
import sodapy

import constants
import data
import transformers


def main():
    """ Pipeline for training/testing
    """

    data_filepath = data_api.load_recent_data()
    df = data_api.load_data(filepath=data_filepath)
    (X, y) = transformers.get_sample_target_data(df)

    # split into training/testing
    # 75/25 training/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    pass
