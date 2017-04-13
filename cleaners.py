"""Collection of utility functions meant for cleaning data.

"""


def clean_incident_zip(zipcode):
    """Cleans the 'incident_zip' of the 311 data

    Returns desired format of zipcode
        Rules:
        xxxxx-xxxx --> int(xxxxx)
        na -> 0
        xxx.0 --> 00xxx
    """
    zipcode = str(zipcode).replace('.0', '')[:5]
    try:
        zipcode = int(zipcode)
    except:
        return None
    # Pad it on the left with '0's
    zipcode = '{:05}'.format(zipcode)
    return zipcode
