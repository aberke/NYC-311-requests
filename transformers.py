"""Utility functions to transform data.

"""

import dateutil

import numpy as np
import pandas as pd

import constants
from cleaners import (
    clean_incident_zip
)


def common_transformations(df):
    """ Applies transformations to data frame that are used for all incoming data
    including training, test, and new data to classify

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

    # Expand by time of day
    df['created_hr_of_day'] = df['created_date'].dt.hour
    hour_of_day_dummies = pd.get_dummies(df['created_hr_of_day'], prefix='created_hr_of_day')
    df = pd.concat([df, hour_of_day_dummies], axis=1)

    # Expand by day of the week
    df['created_day_of_week'] = df['created_date'].dt.weekday_name
    day_of_week_dummies = pd.get_dummies(df['created_day_of_week'], prefix='created_day_of_week')
    df = pd.concat([df, day_of_week_dummies], axis=1)

    # Expand by month
    df['created_month'] = df['created_date'].dt.month
    month_dummies = pd.get_dummies(df['created_month'], prefix='created_month')
    df = pd.concat([df, month_dummies], axis=1)

    # Expand complaint type
    complaint_type_dummies = pd.get_dummies(df['complaint_type'], prefix='complaint_type')
    df = pd.concat([df, complaint_type_dummies], axis=1)

    # Expand community board
    community_board_dummies = pd.get_dummies(df['community_board'], prefix='community_board')
    df = pd.concat([df, community_board_dummies], axis=1)

    # Drop all of the columns we manipulated or used as interim columns
    drop_columns = [
        'agency',
        'incident_zip',
        'created_hr_of_day',
        'created_day_of_week',
        'created_month',
        # Created date MUST be dropped, but later
        'complaint_type',
        'community_board'
    ]
    df.drop(drop_columns, axis=1, inplace=True)

    return df


def transform_test_and_training(df):
    """Applies necessary transformers for both test and training data """
    
    # Drop data that has no closed date
    df.dropna(subset=['closed_date'], inplace=True)

    # Drop data whith invalid closed date where closed_date < created_date
    df = df.drop(df[df.closed_date - df.created_date < pd.Timedelta(0)].index)

    df = common_transformations(df)


    return df


def get_sample_target_data(df):
    """ Transforms the data as training/target data.

    Returns (X, y)
    where X is the feature set, y is the target/category
    """

    df = transform_test_and_training(df)

    # Get a series as a timedelta of open period in hours
    target_open_hours = (df.closed_date - df.created_date) / pd.Timedelta(hours=1)
    # Transform that series of hours into labeled categories
    target_bin_mapping = {
        1: '< 1 hr',
        3: '1 - 3 hrs',
        6: '3 - 6 hrs',
        12: '6 - 12 hrs',
        24: '12 - 24 hrs',
        36: '24 - 36 hrs',
        48: '36 - 48 hrs',
        168: '2 - 7 days',
        672: '1 - 4 weeks',
        1000000: '> 4 weeks',
    }
    target_bins = [0] + list(target_bin_mapping.keys())
    target_labels = list(target_bin_mapping.values())
    target = pd.cut(target_open_hours, bins=target_bins, labels=target_labels)
    y = target
    
    # Remove from X the closed_dates -- it would ruin testing/training
    df.drop([
        'closed_date',
        'created_date',
    ], axis=1, inplace=True)
    X = df

    return (X, y)


def get_open_period(data_row):
    """Returns timedelta representing time between created_date and closed_date
    or None if not closed.
    """
    closed_date = data_row[constants.CLOSED_DATE]
    created_date = data_row[constants.CREATED_DATE]
    if isinstance(closed_date, str) and isinstance(created_date, str): # Missing data is np.nan type and will evaluate to False
        closed_datetime = dateutil.parser.parse(closed_date)
        created_datetime = dateutil.parser.parse(created_date)
        return closed_datetime - created_datetime


def format_date(datetime):
    return datetime.strftime("%Y-%m-%d")
