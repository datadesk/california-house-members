# california-house-members

A simple machine-readable list of the 53 men and women California sends to Congress.

* [CSV](./california-house-members.csv)
* [GeoJSON](./california-house-members.geojson)

Data are accurate as of Nov. 5, 2015 and not guaranteed to update.

## How to update

To update or expand metadata about a member edit the [CSV file](./california-house-members.csv)
and rerun the python command that merges it with the [district boundaries](./2011-districts.geojson).

```bash
$ python merge-csv-to-districts.py
```

That will create a new combined GeoJSON file at [california-house-members.geojson](./california-house-members.geojson).
Commit that and push it to the repository to complete an update.
