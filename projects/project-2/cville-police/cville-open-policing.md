# Charlottesville Open Data – Policing


**Arrests** Reference: <https://opendata.charlottesville.org/datasets/arrests>
**Crime** Reference: <https://opendata.charlottesville.org/datasets/crime-data/>

Helpful code below! Note: Remember to replace `df.COLUMN` with the column containing values you'd usually enter into something like Google Maps 

```python
# Import package to help search locations
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="myGeocoder")

# Helper function to pull helpful points
def grab_geodata(x):
    try:
        geo = geolocator.geocode(x)
        geo_data = (geo.latitude, geo.longitude, geo.address)
        return geo_data
    except:
        return ('null','null','null')

# Grab geo data for all rows, may take a while
df['geo_data'] = df.COLUMN.apply(grab_geodata)

# Parse the output and save to individual columns
df['lat'] = df.geo_data.apply(lambda x: x[0])
df['lon'] = df.geo_data.apply(lambda x: x[1])
df['address'] = df.geo_data.apply(lambda x: x[2])
```