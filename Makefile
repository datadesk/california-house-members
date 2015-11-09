.PHONY: simplify

simplify:
	ogr2ogr -f "GeoJSON" 2011-districts-simplified.geojson 2011-districts.geojson -simplify 100
