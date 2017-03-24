"""Data retrievers.

"""

from datetime import (
    datetime,
    timedelta,
)


import numpy
import pandas
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
    


def get_data_between_dates(from_date=None, to_date=None, limit=REQUEST_LIMIT):
    """TODO
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
    return pandas.DataFrame(data)

