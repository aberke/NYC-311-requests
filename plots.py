"""Do stuff with maps and plots.


X axis: Community Board
Y axis:
    - # total requests
    - # requests closed
    - # avg open period time (in hours)

"""

import numpy as np
import matplotlib.pyplot as plt

import constants
import data_api
import explore


AGENCIES_TO_HANDLE = ["NYPD", "DOB"]


def main():

    # Get data from the start of the year
    data = data_api.load_recent_data()
    # Segment by agency
    # - Do that here so to ignore data with agencies don't care about
    for agency in AGENCIES_TO_HANDLE:
        agency_data = data[data[constants.AGENCY] == agency]
        print("handling {} rows for agency: '{}'".format(len(agency_data), agency))
        handle_data(agency_data)


def add_open_period_column(data_frame):
    # add open_time column
    open_periods = explore.get_open_periods(data_frame)
    data_frame = data_frame.assign(open_period=open_periods.values)
    return data_frame


def handle_data(data_frame):
    print("handle data for {} rows".format(len(data_frame)))

    print("columns before adding open_period: ", len(data_frame.columns))
    data_frame = add_open_period_column(data_frame)
    print("columns after adding open_period: ", len(data_frame.columns))

    # TODO: remove data where open_time not between %5 and 95% quantiles

    # add closed boolean (0/1) column
    data_frame['closed'] = data_frame['closed_date'].apply(lambda x: 1 if isinstance(x, str) else 0)

    # Will fill up this dictionary
    # community_boards_data = {
    #     cb_name: cb_data for cb in community boards 
    # }
    community_boards_data = {}

    # Segment by community boards
    for cb_name in constants.COMMUNITY_BOARD_VALUES:
        cb_data = data_frame[data_frame[constants.COMMUNITY_BOARD] == cb_name]
        community_boards_data[cb_name] = cb_data

    # Make a plot from community_boards_data!

    # handle plotting
    colors = ['red', 'tan', 'lime']


    # handle by agency
    return community_boards_data




