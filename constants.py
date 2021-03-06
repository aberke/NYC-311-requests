"""Constants file

"""

# Column names/Keys
DUE_DATE = "due_date"
CLOSED_DATE = "closed_date"
CREATED_DATE = "created_date"


# When reading the data into pandas, read these in as date fields
READ_AS_DATE_FIELDS = [
    CLOSED_DATE,
    CREATED_DATE,
    DUE_DATE,
]

AGENCY = "agency"

# data["agency"].unique()
AGENCY_VALUES = [
    "NYPD",
    "DOT",
    "DPR",
    "DOHMH",
    "DEP",
    "DOF",
    "HRA",
    "DOITT",
    "TLC",
    "DCA",
    "HPD",
    "DSNY",
    "DHS",
    "DOB",
    "DFTA",
    "DOE",
    "FDNY",
    "3-1-1",
    "NYCEM",
]

COMPLAINT_TYPE = "complaint_type"

COMMUNITY_BOARD = "community_board"


# from "community_board" key
COMMUNITY_BOARD_VALUES = [
    "10 QUEENS",
    "11 QUEENS",
    "0 Unspecified",
    "15 BROOKLYN",
    "08 BRONX",
    "05 QUEENS",
    "06 MANHATTAN",
    "08 BROOKLYN",
    "07 MANHATTAN",
    "12 MANHATTAN",
    "14 BROOKLYN",
    "08 MANHATTAN",
    "08 QUEENS",
    "12 BRONX",
    "06 BRONX",
    "05 BROOKLYN",
    "03 STATEN ISLAND",
    "13 QUEENS",
    "04 BRONX",
    "10 BROOKLYN",
    "11 MANHATTAN",
    "01 BROOKLYN",
    "04 QUEENS",
    "09 QUEENS",
    "03 BROOKLYN",
    "17 BROOKLYN",
    "03 MANHATTAN",
    "10 MANHATTAN",
    "02 MANHATTAN",
    "07 QUEENS",
    "13 BROOKLYN",
    "02 QUEENS",
    "04 MANHATTAN",
    "07 BROOKLYN",
    "05 BRONX",
    "05 MANHATTAN",
    "06 QUEENS",
    "14 QUEENS",
    "09 BRONX",
    "01 QUEENS",
    "07 BRONX",
    "11 BROOKLYN",
    "06 BROOKLYN",
    "03 QUEENS",
    "03 BRONX",
    "09 BROOKLYN",
    "12 QUEENS",
    "10 BRONX",
    "09 MANHATTAN",
    "02 STATEN ISLAND",
    "04 BROOKLYN",
    "02 BROOKLYN",
    "16 BROOKLYN",
    "Unspecified BROOKLYN",
    "18 BROOKLYN",
    "12 BROOKLYN",
    "02 BRONX",
    "01 BRONX",
    "11 BRONX",
    "01 STATEN ISLAND",
    "01 MANHATTAN",
    "Unspecified MANHATTAN",
    "Unspecified BRONX",
    "Unspecified QUEENS",
    "81 QUEENS",
    "83 QUEENS",
    "Unspecified STATEN ISLAND",
    "56 BROOKLYN",
    "28 BRONX",
    "55 BROOKLYN",
    "80 QUEENS",
    "95 STATEN ISLAND",
    "26 BRONX",
    "82 QUEENS",
    "27 BRONX",
    "64 MANHATTAN",
    "84 QUEENS"
]
