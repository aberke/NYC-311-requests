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




## Steps

### Prep training data

	- universal to all data, test and training

	- training data

- drop all samples not yet closed
- expand features into binary values with pandas.get_dummies
	- zipcode
	- agency



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

- Not all people harboring bees are beekeepers
	- since the start of 2017, there have been 3 unique bee complaints
	- 2 complaints were closed as of then
	- these occurred in separate boroughs

