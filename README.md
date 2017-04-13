# NYC-311-requests
Civic Hacking + Data Science


### Development

- Set up for the first time
  - `$ virtualenv venv`

And then always

- `$ source venv/bin/activate`
- `$ pip install -r requirements.txt`



### Data Source

[NYC 311 Requests](https://data.cityofnewyork.us/Social-Services/311/wpe2-h2i5)

> All 311 Service Requests from 2010 to present. This information is automatically updated daily.


### Data via api

#### Use Socrata's API wrapper

- sodapy
- [Docs](https://github.com/xmun0x/sodapy)

#### Using Raw requests:

Raw API endpoint: https://data.cityofnewyork.us/resource/wpe2-h2i5.json

[Docs for API endpoint](https://dev.socrata.com/foundry/data.cityofnewyork.us/fhrw-4uyv)


Example Request to get rows between dates:
- GET https://data.cityofchicago.org/resource/6zsd-86xi.json?$where=date between '2016-03-20T12:00:00' and '2016-03-22T12:00:00'


"Datetimes":

- eg, created_at
- They are "Floating Timestamps".  [See docs](https://dev.socrata.com/docs/datatypes/floating_timestamp.html)
- Floating timestamps represent an instant in time with millisecond precision, with no timezone value, encoded as ISO8601 Times with no timezone offset. When writing data, accuracy to only the second is required, but the service will always return precision to the millisecond.

- For example:
	[ {
	  "date_time_column": "2014-10-13T00:00:00.000"
	} ]


Example Request to get item by unique key

https://data.cityofnewyork.us/resource/fhrw-4uyv.json?unique_key=35752674


## Time buckets/categories for the classifier

Unit: hours
- < 1
- 1-3
- 3-6
- 6-12
- 12-24
- 24-36
- 36-48
- 48-72
- 72-168 # 3 days to 1 week
- 168-672 # 1 week to 4 weeks
- > 672 # More than 4 weeks


## Steps

### Prep training data

	- universal to all data, test and training

	- training data

- expand features into binary values with pandas.get_dummies
    - zipcode
    - agency

- drop all samples not yet closed

- decide on categories
	- categorize training data by open_period

- assign categories to training data based on open_period

- decide on model to use
- train model

    

- get best features from model

- retrain with these features for linear regression

- maybe use those features for linear regression model
	- to get more precise closed date





### Notes


- Some requests are closed in less than 2 minutes -- what does this mean?
    - Most are closed with mesage like "your request was received"

    - (top) 1000s are 'complaint_type' == 'Benefit Card Replacement'  Nearly all records are closed instantaneously
        - They're all closed wit ha description that the HRA has "received your request..".
    - 1000's have the complaint_type == 'Derelict Vehicle'
        -- all closed by the Department of Sanitation
        - Makes sense: http://www1.nyc.gov/nyc-resources/service/989/abandoned-vehicle

    - 1000's have complaint_type == "Street Light Condition"
        - All that are closed within 2 mins are assigned to the DOT with "resolution_description" that the "status for this request is available on the DOT website.... " etc

    - Many have complaint_type of "Building/Use"
        - Most resolution descriptions have the same message that the request has been submitted to the DOB


- "Snow" is a Dept of Sanitation agency issue.


- Not all people harboring bees are beekeepers
	- since the start of 2017, there have been 3 unique bee complaints
	- 2 complaints were closed as of then
	- these occurred in separate boroughs

