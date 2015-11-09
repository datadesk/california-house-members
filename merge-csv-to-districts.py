"""
Merges the CSV data about members with a GeoJSON of the districts.
"""
import csv
import json


if __name__ == "__main__":
    # Paths
    district_path = "2011-districts-simplified.geojson"
    csv_path = "california-house-members.csv"
    output_path = "california-house-members.geojson"

    # Read in district maps and csv data
    district_data = json.load(open(district_path, 'rb'))
    csv_data = csv.DictReader(open(csv_path, 'rb'))

    # Regroup CSV data to be keyed by district number
    csv_dict = dict((int(r['district_number']), r) for r in csv_data)

    # Loop through the district maps
    for feature in district_data['features']:
        # Merge in the CSV data
        csv_row = csv_dict[feature['properties']['district_number']]
        feature['properties'].update(csv_row)

    # Write out the combined file
    json.dump(district_data, open(output_path, 'w'))
