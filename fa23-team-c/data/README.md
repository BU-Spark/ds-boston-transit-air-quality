# Data Explanations #

## Data Sources ##
 
#### <ins> Proximity to Roads ####
- File name: [mapc.health_mapc_ppi_g250](/fa23-team-c/data/roadProximity).
- A shapefile of the 250-meter gridded population data with associated PPI scores.
- Gridded population by race, categorized by Pollution Proximity Intensity (PPI), a weighted measure of intensity of roadway vehicle emissions of nitrogen oxides (NOx).
- Source: Metropolitan Area Planning Council (MAPC) and the Boston University School of Public Health (BUSPH)
- Link: https://datacommon.mapc.org/browser/datasets/413

    `Summary:` In a study of the MAPC region, researchers examined where residents live in relation to high-pollution roads, focusing on households within 150 meters. They introduced the Pollution Proximity Index (PPI) that considers traffic factors and proximity to pollution sources. High PPI areas often have busy roadways, especially freeways and main roads with diesel vehicles. (more details on Google Drive). 

#### <ins> Climate Ready Boston Social Vulnerability ####
- File name: [Climate_Ready_Boston_Social_Vulnerability.csv](/fa23-team-c/data/socialVulnerability/)
- A csv file describes number of vulnerable groups in different neighborhoods in Boston. 
- Attributes (not mentioned above):
    - GEOID10: Geographic identifier: State Code (25), Country Code (025), 2010 Census Tract
    - AREA_SQFT/AREA_ACRES: Tract area (in square feet/acres)
    - POP100_RE: Tract population count
    - HU100_RE: Tract housing unit count
    - Name: Boston Neighborhood
- Source: Climate Ready Boston
- Link: https://data.boston.gov/dataset/climate-ready-boston-social-vulnerability

    `Summary:` Social vulnerability is defined as the disproportionate susceptibility of some social groups to the impacts of hazards, including death, injury, loss, or disruption of livelihood. In this dataset from Climate Ready Boston, groups identified as being more vulnerable are older adults, children, people of color, people with limited English proficiency, people with low or no incomes, people with disabilities, and people with medical illnesses. 

#### <ins> Air quality sensor data ####

- Link: https://www.arcgis.com/apps/dashboards/7ee4b278406445d7b8d487a49a2d88d9

    `Summary:` The dashboard displays data from outdoor air quality sensors around Boston, measuring variables such as PM2.5, PM10.0, Carbon Monoxide (CO), Nitrogen Dioxide (NO2), Sulfur Dioxide (SO2), VOC (Volatile Organic Compounds), AQI (Air Quality Index), Ozone, Relative Humidity, Temperature, and Pressure


### Census Data for Demographics ####

- Link: https://www.census.gov/programs-surveys/acs/data.html 

    `Summary:` Has a bunch of tools that may help with analyzing data: Geometric Comparison Table (Geographic Comparison Tables allow users to compare ACS data across geographic areas in the same table. ACS Geographic Comparison Tables begin with the letters "GCT.")

    - Geometric Comparison Table: https://www.census.gov/acs/www/data/data-tables-and-tools/geographic-comparison-tables/


## Raw Data ##
AirNow Daily Data: .zip file inside team shared drive