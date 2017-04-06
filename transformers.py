"""Utility functions to transform data.

"""

import dateutil

import numpy
import pandas

import constants
from cleaners import (
    clean_zip
)


def transform_test_and_training(df):
    """Applies necessary transformers for both test and training data


    FLAG: Will scikit learn handle 'sparse vectors' in this way?
    For example, a df with one row will not know about the other columns
    for zip code -- the transformed df will leave in a different space then
    from the training data -- is this okay?
    """

    # Expand values into binary features

    # Expand agency
    agency_dummies = pd.get_dummies(df['agency'], axis=1)
    df = pd.concat(df, agency_dummies)

    # Clean and expand incident_zip codes
    incident_zip = df.incident_zip.apply(clean_incident_zip)
    zip_dummies = pd.get_dummies(incident_zip, prefix='incident_zip')
    df = pd.concat(df, zip_dummies, axis=1)

    # Expand by day of the week
    df['created_day_of_week'] = df['created_date'].dt.weekday_name
    day_of_week_dummies = pdf.get_dummies(df['created_day_of_week'])
    df = pd.concat([df, day_of_week_dummies])

    # Expand by month
    df['created_month'] = df['created_date'].dt.month
    month_dummies = pdf.get_dummies(df['created_month'])
    df = pd.concat([df, month_dummies])

    # Expand complaint type
    complaint_type_dummies = pd.get_dummies(df[constants.COMPLAINT_TYPE], prefix=constants.COMPLAINT_TYPE)
    df = pd.concat([df, complaint_type_dummies], axis=1)

    # Expand community board
    community_board_dummies = pd.get_dummies(df[constants.COMMUNITY_BOARD], prefix=constants.COMMUNITY_BOARD)
    df = pd.concat([df, community_board_dummies], axis=1)

    return df


def transform_training_data(df):
    """Applies necessary transformers for training data only """
    df = transform_test_and_training(df)
    
    # Drop close date -- TODO
    pass



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
    """Returns timedelta representing time between created_date and closed_date
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
