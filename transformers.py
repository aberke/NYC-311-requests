"""Utility functions to transform data.

"""

import dateutil

import numpy as np
import pd

import constants
from cleaners import (
    clean_incident_zip
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
    agency_dummies = pd.get_dummies(df['agency'])
    df = pd.concat([df, agency_dummies], axis=1)

    # Clean and expand incident_zip codes
    incident_zip = df.incident_zip.apply(clean_incident_zip)
    zip_dummies = pd.get_dummies(incident_zip, prefix='incident_zip')
    df = pd.concat([df, zip_dummies], axis=1)

    # Expand by day of the week
    df['created_day_of_week'] = df['created_date'].dt.weekday_name
    day_of_week_dummies = pd.get_dummies(df['created_day_of_week'])
    df = pd.concat([df, day_of_week_dummies], axis=1)

    # Expand by month
    df['created_month'] = df['created_date'].dt.month
    month_dummies = pd.get_dummies(df['created_month'], prefix='month')
    df = pd.concat([df, month_dummies], axis=1)

    # Expand complaint type
    complaint_type_dummies = pd.get_dummies(df['complaint_type'], prefix='complaint_type')
    df = pd.concat([df, complaint_type_dummies], axis=1)

    # Expand community board
    community_board_dummies = pd.get_dummies(df['community_board'], prefix='community_board')
    df = pd.concat([df, community_board_dummies], axis=1)

    return df


def transform_training_data(df):
    """Applies necessary transformers for training data only """
    df = transform_test_and_training(df)
    
    # TODO
    # Drop data that has no closed date
    
    # Drop data whith invalid closed date where closed_date < created_date
    

    pass



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
