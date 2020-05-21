import json

with open('zillow-neighborhoods.geojson', 'r') as infile:
    input_dict = json.load(infile)
    
input_dict['features'] = [x for x in input_dict['features'] if x['properties']['city'] == 'Seattle']


with open('zillow-neighborhoods3.geojson', 'w') as outfile:
    json.dump(input_dict, outfile)    