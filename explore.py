""" TODO
"""

from datetime import (
    datetime,
    timedelta,
)


import numpy
import pandas
import sodapy

import constants
import data
import transformers




def get_open_periods(data):
    open_periods = []
    for index, data_row in data.iterrows():
        open_period = transformers.get_open_period(data_row)
        open_periods.append(open_period)

    return pandas.Series(open_periods)


def main():
    """
    get_data from this year
        - drop data without closed_date
    transform it
        - column for each agency
        - column for each zipcode
        - column for each other thing that is non numerical
        - column for day of the week
        - column for month name
        - column for time of day reported   
    """
    year_data = load_recent_data()
    # ignore data that has no closed_date
    year_data = year_data.dropna(subset=[constants.CLOSED_DATE])

    # Apply transformers
    # Expand agency data
    transformers.data_expand_agency(data)


    # Later, when take in one row at a time, can do
    # row_data = pandas.DataFrame([row_data])
    
    pass













