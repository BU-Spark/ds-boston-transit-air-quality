
# Essential Files
- DataByNeighborhood.csv - Summarized file with all essential information
- VisualMap.html - Visual summary of information on map of Boston
- Files under the Google AQI Folder, Health Data Folder, and Extension Folder have most up-to-date data and analysis.

# Datasets:
- [Proximity to Roads:](https://www.mapc.org/wp-content/uploads/2020/05/PPA_Technical_Memorandum.pdf) Examined the correlation between community types and the Proximity to Roads (PPI) Index, assessing how communities relate to road networks.
- [Air Quality Data from Google Maps:](https://support.google.com/maps/answer/11270845?hl=en) Air Quality data including AQI, PM, SO2, NO2, and O3 across various areas in Boston pulled from AirNow and PurpleAir.
- [MBTA Transit Data:](https://boston.maps.arcgis.com/home/item.html?id=fda29d2d98ff427588064375c5c9afe5) Geolocation of Trolley (T) stops across Boston
- [Census Data:](https://www.census.gov/programs-surveys/acs/data.html) ACS census data from U.S. Census Bureau for every census tract and Boston neighborhood in Suffolk County.
- [Social Vulnerability:](https://data.boston.gov/dataset/climate-ready-boston-social-vulnerability) Information divided by tracts on groups more likely vulnerable to impacts of hazards, including death, injury, loss, or disruption of livelihood.
- Health Dataset: CDC Data by Zip Code of prevalence of relevant health conditions such as Asthma and Physical Health.
- [MBTA Bus Stops:](https://www.mass.gov/info-details/massgis-data-mbta-bus-routes-and-stops) Geolocations of Bus Stops across Boston.
- [Blue Bikes Data:](https://bluebikes.com/system-data) Number of Blue Bikes stations and docks across Boston.
- [Open Spaces and Green Spaces:](https://data.boston.gov/dataset/open-space) Information on the number of open spaces and parks in each neighborhood.
- [Boston Neighborhoods Profile:](https://www.bostonplans.org/getattachment/f719d8d1-9422-4ffa-8d11-d042dd3eb37b) Population by Age, Labor Force, Payroll Jobs, Vehicle Ownership


# Data Definitions

## Demographic Information:

- `TotChild`: Total number of children in the neighborhood.
- `OlderAdult`: Total number of older adults in the neighborhood.
- `MedIllnes`: Number of individuals with medical illnesses in the neighborhood.
- `POC2`: Percentage of people of color in the neighborhood.
- `LEP`: Number of individuals with Limited English Proficiency in the neighborhood.
- `Low_to_No`: Percentage of individuals with low to no income in the neighborhood.
- `TotDis`: Total number of individuals with disabilities in the neighborhood.

## Environmental Information:

- `NO2`: Concentration of Nitrogen Dioxide in the air.
- `O3`: Concentration of Ozone in the air.
- `PM10`: Concentration of Particulate Matter (PM10) in the air.
- `PM2.5`: Concentration of Particulate Matter (PM2.5) in the air.
- `SO2`: Concentration of Sulfur Dioxide in the air.
- `AQI`: Air Quality Index representing the overall air quality.
- `Category`: Air quality category based on AQI.

## Transportation Information:

- `T Stops Count`: Total number of T (Trolley) stops in the neighborhood.
- `Bus Stops Count`: Total number of bus stops in the neighborhood.
- `Blue Bikes Stations Count`: Total number of Blue Bikes stations in the neighborhood.
- `Blue Bikes Docks Count`: Total number of Blue Bikes docks in the neighborhood.

## Health Information:

- `CASTHMA CrudePrev`: Crude prevalence of Asthma in the neighborhood.
- `COPD CrudePrev`: Crude prevalence of Chronic Obstructive Pulmonary Disease (COPD) in the neighborhood.
- `CHD CrudePrev`: Crude prevalence of Coronary Heart Disease (CHD) in the neighborhood.
- `STROKE CrudePrev`: Crude prevalence of Stroke in the neighborhood.
- `HIGHCHOL CrudePrev`: Crude prevalence of High Cholesterol in the neighborhood.
- `GHLTH CrudePrev`: Crude prevalence of Good Health in the neighborhood.
- `PHLTH CrudePrev`: Crude prevalence of Poor Health in the neighborhood.
- `MHLTH CrudePrev`: Crude prevalence of Mental Health issues in the neighborhood.
- `CSMOKING CrudePrev`: Crude prevalence of Cigarette Smoking in the neighborhood.
- `BINGE CrudePrev`: Crude prevalence of Binge Drinking in the neighborhood.
- `LPA CrudePrev`: Crude prevalence of Physical Inactivity in the neighborhood.
- `OBESITY CrudePrev`: Crude prevalence of Obesity in the neighborhood.
- `SLEEP CrudePrev`: Crude prevalence of Insufficient Sleep in the neighborhood.

## Other Information:

- `Num Parks`: Total number of parks in the neighborhood.
- `Payroll Jobs`: Total number of payroll jobs in the neighborhood.
- `Labor Force`: Total labor force in the neighborhood.
- `At least one vehicle (%)`: Percentage of households with at least one vehicle in the neighborhood.
- `Vehicles to Households Ratio`: Ratio of vehicles to households in the neighborhood.





