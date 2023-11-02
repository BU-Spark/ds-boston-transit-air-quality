# Data Explanation #

#### <ins>MAPC Health and Pollution Proximity Intensity Data</ins>
- File name: [pollution_proximity_intensity.csv](/fa23-team-a/data/csv_files/pollution_proximity_intensity.csv)
- Description: This dataset encapsulates the demographic distribution within Boston's 250-meter grid cells and associates each cell with a Pollution Proximity Intensity (PPI) score.
- Data content: Populational statistics by race within the designated grid cells are coupled with a PPI score, indicating the level of exposure to vehicle emission-related pollutants, predominantly nitrogen oxides (NOx).
    - nhwhi_10: Non-Hispanic White
    - nhaa_10: Non-Hispanic African American
    - nhapi_10: Non-Hispanic Asian Pacific Islander
    - lat_10: Latino
    - nhoth_10: Non-Hispanic Other
- Source: The data is compiled and made available by the Metropolitan Area Planning Council (MAPC).
- Link: https://datacommon.mapc.org/browser/datasets/413

    `Summary:` The MAPC Health and PPI dataset is a vital resource for analyzing the intersection of urban demographics and environmental stressors, such as air pollution from vehicular emissions. The PPI scores offer a nuanced understanding of pollution exposure risks, which can significantly affect public health, especially in densely populated urban areas. By cross-referencing the PPI scores with health outcome data, researchers can identify patterns and trends, potentially guiding public policy and urban development towards healthier living environments.



#### <ins>Boston Demographic and Environmental Data</ins>
- File name: [boston_dem.csv](/fa23-team-a/data/boston_dem.csv)
- Description: This dataset provides detailed demographic information along with environmental data for various areas within Boston. It quantifies population characteristics, housing units, age distribution, proximity to pollutants, and more.
- Data content: The dataset includes demographic statistics like total population, housing units, and age-related demographics, as well as environmental data points such as particulate matter measurements. Key columns are:
    - `POP100_RE`: Total population
    - `HU100_RE`: Housing units
    - `MedIllnes`: Median illness index
    - `pm2.5_atm`: Atmospheric particulate matter with a diameter of less than 2.5 micrometers
    - `pm10_atm`: Atmospheric particulate matter with a diameter of less than 10 micrometers
- Source: Combined sources from Purple Air and Climate_Ready_Boston_Social_Vulnerability.geojson

    `Summary:` The Boston Demographic and Environmental Data set serves as a comprehensive tool for understanding the socio-demographic layout of Boston in relation to environmental factors such as air quality. The inclusion of particulate matter readings offers insights into the potential respiratory and health risks associated with different areas. This data can be instrumental for urban planners, health researchers, and policymakers in assessing the impact of environmental conditions on various populations, guiding targeted interventions, and improving urban health outcomes.




#### <ins>Census Data for Demographics</ins>
- File name: [Selected_Economic_Characteristics.csv](/fa23-team-a/data/csv_files/Selected_Economic_Characteristics.csv).
- File name: [Selected_Housing_Characteristics.csv](/fa23-team-a/data/csv_files/Selected_Housing_Characteristics.csv).
- File name: [Selected_Social_Characteristics.csv](/fa23-team-a/data/csv_files/Selected_Social_Characteristics.csv).
- Description: The U.S. Census Bureau's data portal provides a wealth of demographic, economic, and housing data collected from across the United States.
- Data content: The portal includes datasets from the Decennial Census, the American Community Survey, and various other studies and assessments conducted by the U.S. Census Bureau. It covers a broad range of topics such as population demographics, income, education, employment, housing characteristics, and more.
- Source: All data is collected and maintained by the U.S. Census Bureau.
- Link: https://data.census.gov/

    `Summary:` The datasets available through the U.S. Census Bureau's data portal are invaluable for understanding the social and economic makeup of neighborhoods, cities, states, and the nation as a whole. These datasets allow for comprehensive socio-economic analyses, enabling policymakers, researchers, and the public to make informed decisions based on current and historical data. The breadth and depth of information available support a wide range of applications, from public policy formulation to market research, urban development, and beyond.



#### <ins>Social Vulnerability Index</ins>
- File name: [Climate_Ready_Boston_Social_Vulnerability.csv](/fa23-team-a/data/csv_files/Climate_Ready_Boston_Social_Vulnerability.csv).
- Description: This dataset offers a comprehensive view of the social vulnerability factors across Boston neighborhoods, which can affect residents' ability to respond to and recover from hazardous events and environmental stresses.
- Data content: Key indicators in the dataset include demographic, socio-economic, and housing characteristics that contribute to the overall social vulnerability score for each area.
- Source: The data has been collated and provided by the Climate Ready Boston initiative.
- Link: https://data.boston.gov/dataset/climate-ready-boston-social-vulnerability

    `Summary:` The Social Vulnerability Index presented in this dataset is instrumental in pinpointing neighborhoods with populations that may be disproportionately affected by events such as extreme weather, public health emergencies, and other crises. The index includes various metrics that reflect the population's age distribution, income levels, language proficiency, and other factors crucial for emergency preparedness and resource allocation. By leveraging this data, city planners, health officials, and community organizations can better understand and address the needs of Boston's most vulnerable groups.

