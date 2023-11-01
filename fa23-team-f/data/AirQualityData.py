import requests
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from io import StringIO
import time
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Base URL and API Key
base_url = "https://www.airnowapi.org/aq/observation/zipCode/historical/"
api_key = "11AD4349-C7D6-4B5D-AB88-2C96AA83B881"

start_date = datetime(2023, 1, 11)
end_date = datetime(2023, 4, 1)


zip_codes = [
    '02134', '02125', '02110', '02118', '02126', '02109', '02113', '02130', '02121',
    '02119', '02115', '02163', '02135', '02199', '02124', '02132', '02114', '02108',
    '02136', '02111', '02210', '02116', '02131', '02127', '02120', '02203', '02215',
    '02129', '02128', '02122', '02151', '02467'
]


df = pd.DataFrame()
uszips = pd.read_csv('uszips.csv')
def zip_to_coordinates(zip:str):
    partial_zip = zip[1:]
    row = uszips.loc[uszips['zip'] == int(partial_zip)]
    if row.empty:
        print("Error, can't make transitions")
        return 
    else:
        return [row['lat'],row['lng']]
    
# print(zip_to_coordinates('02215')[0])



for zip_code in zip_codes:
    current_date = start_date
    while current_date < end_date:
        date_str = current_date.strftime('%Y-%m-%dT00-0000')
        params = {
            "format": "text/csv",
            "zipCode": zip_code,
            "date": date_str,
            "distance": 25,
            "API_KEY": api_key
        }

        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            if response.text.strip():  # Check if response is not empty
                print(f"Data for {current_date.strftime('%Y-%m-%d')} and ZIP Code {zip_code} received.")
                try:
                    data = pd.read_csv(StringIO(response.text))
                    if not data.empty:
                        # if data['ReportingArea'][0] == "Boston":
                        data['zipCode'] = zip_code
                        lat = data['Latitude'][0]
                        Coordinates = zip_to_coordinates(zip_code)
                        if Coordinates == None:
                            print("Error in converting to coordinates for zip: " + zip_code)
                            df = pd.concat([df, data], ignore_index=True)
                        else:
                            for i in range(0,len(data['Latitude'])):
                                data.at[i,'Latitude'] = Coordinates[0]
                                data.at[i,'Longitude'] = Coordinates[1]
                            df = pd.concat([df, data], ignore_index=True)
                        # else:
                        #     print("Received data outside of Boston")
                    else:
                        print(f"Received empty data for {current_date.strftime('%Y-%m-%d')} and ZIP Code {zip_code}.")
                except pd.errors.EmptyDataError:
                    print(f"No content in CSV for {current_date.strftime('%Y-%m-%d')} and ZIP Code {zip_code}.")
            else:
                print(f"No content received for {current_date.strftime('%Y-%m-%d')} and ZIP Code {zip_code}.")
        else:
            print(f"Error {response.status_code} for ZIP Code {zip_code}: {response.text}")

        time.sleep(8)  # Sleep to respect the API's rate limit
        current_date += timedelta(days=1)


if df.empty:
    print("No data collected.")
else:
    df.to_csv("air_quality_data.csv", index=False)
    print("Data exported to air_quality_data.csv")
