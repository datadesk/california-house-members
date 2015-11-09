.PHONY: simplify merge build

simplify:
	rm ./2011-districts-simplified.geojson
	ogr2ogr -f "GeoJSON" 2011-districts-simplified.geojson 2011-districts.geojson -simplify 0.001

merge:
	python merge-csv-to-districts.py

build:
	make simplify
	make merge
