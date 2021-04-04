# Plane database

The aircraft's model, type, registration and operator are not available in the ADS-B data the aircraft transmits and needs to be pulled from another data source. These are hard to come by as no public database exists that allows robots, to my knowledge. You will need to do some scraping.

This git contains a "Plane database server" you need to host by running

```
% ./planedb-serv.py flightdata.sql 31541
```

Starting the script will create an empty sqlite database for you to polulate with whatever scraped data you can find (ico24 -> aircraft type, registration, and operator).

My tools use the planedb.py to pull data from your plane database.
