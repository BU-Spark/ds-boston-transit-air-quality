import requests
import time
import json
import logging
from datetime import datetime, timedelta
import calendar
import sqlite3
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

logging.basicConfig(filename='aqi_script.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


# REPLACE WITH YOUR OWN API KEY
API_KEY = '2DDB1A47-0497-458F-A3B8-C102AF7314A1'
BASE_URL = 'https://www.airnowapi.org/aq/observation/zipCode/historical'  

# zip codes for Boston 
""" 
ZIP_CODES = [
    "02045", "02108", "02109", "02110", "02111", "02113", "02114", "02115", "02116", "02118", 
    "02119", "02120", "02121", "02122", "02124", "02125", "02127", "02128", "02129", "02130", 
    "02131", "02134", "02135", "02138", "02139", "02140", "02141", "02142", "02143", "02144", 
    "02145", "02163", "02170", "02171", "02199", "02210", "02215", "02152", "02458", "02472", 
    "02474", "02476", "02478", "02445", "02446"
]
"""

ZIP_CODES = ['02108', '02109', '02110', '02111', '02113', '02114', '02115', '02116', '02118', '02119', '02120', '02121', 
             '02122', '02124', '02125', '02127', '02128', '02129', '02130', '02131', '02134', '02135', '02163', '02199', 
             '02210', '02215']



#CHANGE THE LIST ACCORDING TO STEP 7 OF THE GOOGLE DOC
#YEARS = ['2022', '2021', '2019', '2018', '2017']
YEARS = ['2017']

conn = sqlite3.connect('2017_aqi_data.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS aqi_data (
    date TEXT,
    zip_code TEXT,
    data TEXT,
    PRIMARY KEY (date, zip_code)
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS script_progress (
    year INTEGER,
    month INTEGER,
    day INTEGER,
    zip_code_index INTEGER
)''')

# check if there's saved progress
cursor.execute('SELECT year, month, day, zip_code_index FROM script_progress')
progress = cursor.fetchone()
if progress:
    year, month, day, zip_code_index = progress
else:
    year, month, day, zip_code_index = int(YEARS[0]), 1, 1, 0
    cursor.execute('INSERT INTO script_progress (year, month, day, zip_code_index) VALUES (?, ?, ?, ?)', (year, month, day, zip_code_index))
conn.commit()

# save script progress
def save_progress(y, m, d, idx):
    cursor.execute('UPDATE script_progress SET year = ?, month = ?, day = ?, zip_code_index = ?', (y, m, d, idx))
    conn.commit()

# save AQI data
def save_data(d, zip_code, data):
    json_data = json.dumps(data)
    cursor.execute('INSERT OR IGNORE INTO aqi_data (date, zip_code, data) VALUES (?, ?, ?)', (d, zip_code, json_data))
    conn.commit()

session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

# fetch data from the API
def fetch_aqi_data(zip_code, date):
    formatted_date = date.strftime('%Y-%m-%dT00-0000')
    try:
        response = session.get(BASE_URL, params={
            'format': 'application/json',
            'zipCode': zip_code,
            'date': formatted_date,
            'distance': '25',
            'API_KEY': API_KEY
        }, timeout=10)

        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        logger.error(f"HTTP error: {errh}, zip code: {zip_code}, date: {date}")
        return None
    except requests.exceptions.ConnectionError as errc:
        logger.error(f"Error Connecting: {errc}, zip code: {zip_code}, date: {date}")
        return None
    except requests.exceptions.Timeout as errt:
        logger.error(f"Timeout Error: {errt}, zip code: {zip_code}, date: {date}")
        return None
    except requests.exceptions.RequestException as err:
        logger.error(f"Unexpected error: {err}, zip code: {zip_code}, date: {date}")
        return None

    return response.json()


def main():
    global year, month, day, zip_code_index

    try:
        # correctly initialize based on saved progress
        current_year_index = YEARS.index(str(year))
        current_zip_code_index = zip_code_index
        current_month = month
        current_day = day

        for year_index in range(current_year_index, len(YEARS)):
            year = int(YEARS[year_index])

            for zip_index in range(current_zip_code_index, len(ZIP_CODES)):
                zip_code = ZIP_CODES[zip_index]
                
                # start from the saved month if we're resuming, otherwise, start from January
                for month in range(current_month, 13):
                    last_day = calendar.monthrange(year, month)[1]

                    # start from the saved day if we're resuming in the middle of a month, otherwise, start from the first
                    for day in range(current_day, last_day + 1):
                        current_date = datetime(year, month, day)
                        aqi_data = fetch_aqi_data(zip_code, current_date)

                        if aqi_data is None:
                            logger.warning(f"No data retrieved for {current_date} and ZIP {zip_code}.")
                            continue

                        save_data(current_date.strftime('%Y-%m-%d'), zip_code, aqi_data)
                        logger.info(f"Data saved for {current_date} and ZIP {zip_code}.")

                        # save progress after each successful fetch
                        save_progress(year, month, day, zip_index)

                        # 8 seconds is the smallest amount of seconds that prevents us from hitting the rate limit. If you still hit the rate limit, you can try increasong this number but 8 seconds worked best for me.
                        time.sleep(8)

                    current_day = 1  # reset to the first day after finishing a month

                current_month = 1  # rese to January after finishing a year

            current_zip_code_index = 0  # reset the zip code index after finishing all zip codes for a year

        logger.info("Data fetching complete.")

    except Exception as e:
        logger.exception(f"An error occurred: {e}")
    finally:
        conn.close()  


if __name__ == "__main__":
    main()