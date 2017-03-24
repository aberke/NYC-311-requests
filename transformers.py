"""Utility functions to transform data.

"""

import dateutil

import numpy
import pandas

import constants


def agency_to_column_name(agency_value):
    return "agency:{}".format(agency_value)


def data_expand_agency(data):
    """Expands the 'agency' column for each data row out into a unique
    column for each unique agency value.
    New columns have keys 'agency:{agency_value}' and values of 0/1

    Returns (DataFrame) transformed data with a new colunn for each
    possible agency value.
    """
    # Get the 'agency' values for each row as a column vector
    data_agency_column = data[constants.AGENCY]

    for agency_value in constants.AGENCY_VALUES:
        column_name = agency_to_column_name(agency_value)
        data[column_name] = pandas.Series([1 if a == agency_value else 0 for a in data_agency_column])
    return data


def get_open_period(data_row):
    """Return timedelta representing time between created_date and closed_date
    or None if not closed.
    """
    closed_date = data_row[constants.CLOSED_DATE]
    created_date = data_row[constants.CREATED_DATE]
    if isinstance(closed_date, str) and isinstance(created_date, str): # Missing data is numpy.nan type and will evaluate to False
        closed_datetime = dateutil.parser.parse(closed_date)
        created_datetime = dateutil.parser.parse(created_date)
        return closed_datetime - created_datetime


def format_date(datetime):
    return datetime.strftime("%Y-%m-%d")
