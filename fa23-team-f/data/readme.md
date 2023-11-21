
# Essential Files
- DataByNeighborhood.csv - Summarized file with all essential information
- neighborhood_map.html - Visual summary of information on map of Boston
- Files under the Google AQI and Health Data Folder have most up-to-date data and analysis.

# Data Defintions
## Proximity to Roads (PPI Index)
https://www.mapc.org/wp-content/uploads/2020/05/PPA_Technical_Memorandum.pdf

Gridded population by race, categorized by Pollution Proximity Intensity (PPI), a weighted measure of intensity of roadway vehicle emissions of nitrogen oxides (NOx). Shapefile & CSV.

'nhwhi_10': 'Non-Hispanic White',
'nhaa_10': 'Non-Hispanic African American',
'nhapi_10': 'Non-Hispanic Asian',
'lat_10': 'Latino or Hispanic',
'nhoth_10': 'Non-Hispanic/Other Races'


## Air Quality Sensor Data
https://www.arcgis.com/apps/dashboards/7ee4b278406445d7b8d487a49a2d88d9

Outdoor Air Quality Sensors measuring PM2.5, PM10, and Ozone. Data Gathered using AirNow API.

- air_quality_data_1.csv and air_quality_data_2.csv is data pulled from the AirNow API
- merged_air_quality_data.csv merges the above 2 files
- filtered_air_quality_data.csv has all data for a given day for each zip code in a single line
- air_quality_summary.csv provides the avg air quality for the year by zipcode

## (Updated) Air Quality from Google Maps Air Quality API
Note: All Deliverable 1 Code has been refactored to work with the Google Air Quality Data and new findings will be found udner the AQI folder.
https://support.google.com/maps/answer/11270845?hl=en

Contains 30 day data related to 

Particulate matter, like PM2.5 and PM10
Ozone (O3)
Nitrogen dioxide (NO2)
Sulfur dioxide (SO2)
Carbon monoxide (CO)
US AQI


## Transit Data
https://boston.maps.arcgis.com/home/webmap/viewer.html?layers=fda29d2d98ff427588064375c5c9afe5

MBTA T stops across Boston. Converted to a geojson.

- All the T stops in the boston area, export_mbta_stops.geojson 

## Census Data
https://www.census.gov/programs-surveys/acs/data.html

## Social Vulnerability
https://data.boston.gov/dataset/climate-ready-boston-social-vulnerability

Groups more likely vulnerable to impacts of hazards, including death, injury, loss, or disruption of livelihood.

- File with all data: Climate_Ready_Boston_Social_Vulnerability.geojson

## CDC Health Data
https://catalog.data.gov/dataset/places-zcta-data-gis-friendly-format-2020-release-f976e
Definitions: https://www.cdc.gov/places/measure-definitions/index.html

## Bus Data
https://hub.arcgis.com/maps/massgis::mbta-bus-routes-and-stops-1/about?layer=0

## Blue Bikes Data
https://bluebikes.com/system-data

## Merged Data
- Contains a combined map with Air Quality, Transit, and Social Vulnerability data (mergedmap.html)
- CSV file with all key information from Air Quality, Transit, and Social Vulnerability divided by neighborhood. (result.csv)

## Open Spaces Data
https://data.boston.gov/dataset/open-space





