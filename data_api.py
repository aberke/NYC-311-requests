"""Data retrievers.

"""
import os

from datetime import (
    datetime,
    timedelta,
)


import pandas as pd
import sodapy

import constants
import transformers


# TODO?: get a real APP_TOKEN
# Until then, will see warnings:
# WARNING:root:Requests made without an app_token will be subject to strict throttling limits.
APP_TOKEN = None

DOMAIN = "data.cityofnewyork.us"
# name of 311 dataset
RESOURCE = "fhrw-4uyv"


## Never request more than this
REQUEST_LIMIT = 1000000  # 1 million

client = sodapy.Socrata(DOMAIN, APP_TOKEN)


def load_recent_data(from_date=None):
    """Load data since from_date, which defaults to beginning of 2017.
    Returns DataFrame representing data.
    """
    # TODO: put this in a constant?
    from_date = from_date or datetime(year=2017, month=1, day=1)
    return get_data_between_dates(from_date=from_date, to_date=datetime.now())
    

def get_data_between_dates(from_date=None, to_date=None, limit=REQUEST_LIMIT, save_to_dir='data'):
    """Fetches the data and saves to file
    Returns filepath that data saved to
    """
    # By default, get data between yesterday and now
    default_days_apart = 1
    to_date = to_date or datetime.now()
    from_date = from_date or (to_date - timedelta(days=default_days_apart))

    request_limit = min(limit, REQUEST_LIMIT)
    where_clause = "{created_date} between '{from_date}' and '{to_date}'".format(
        created_date=constants.CREATED_DATE,
        from_date=from_date.strftime("%Y-%m-%d"),
        to_date=to_date.strftime("%Y-%m-%d"),
    )
    data = client.get(RESOURCE, limit=request_limit, where=where_clause)

    # Save the data
    filename = "{from_date}-{to_date}.csv".format(
        from_date=from_date.strftime("%Y-%m-%d"),
        to_date=to_date.strftime("%Y-%m-%d"),
    )
    df = pd.DataFrame(data)
    save_to_filepath = os.path.join(save_to_dir, filename)
    df.to_csv(save_to_filepath)
    return save_to_filepath


def load_data(filepath=None):
    """ Loads the data from CSV and parses the dates """
    if not filepath:
        filepath = get_data_between_dates()
    # uses index_col so that reading from CSV does not create new unnecessary and unnamed column
    df = pd.read_csv(filepath, index_col=0, parse_dates=constants.READ_AS_DATE_FIELDS)
    return df

