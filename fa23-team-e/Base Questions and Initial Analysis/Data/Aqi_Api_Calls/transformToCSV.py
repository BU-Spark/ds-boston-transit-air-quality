import sqlite3
import csv

# Specify the name of the database file and the table you want to export
database_file = '2022_daily_aqi_data.db'
table_name = 'aqi_data'  # Change this if your table is named differently

# Specify the name of the output CSV file
csv_file = '2022_daily_aqi_data.csv'

# Connect to the SQLite database
conn = sqlite3.connect(database_file)
cursor = conn.cursor()

# Query to fetch data from the specified table
query = f"SELECT * FROM {table_name};"
cursor.execute(query)

# Fetch the table headers (column names)
headers = [description[0] for description in cursor.description]

# Fetch all rows from the executed query
data_rows = cursor.fetchall()

# Write data to CSV file
with open(csv_file, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write the header
    csv_writer.writerow(headers)
    
    # Write the data
    csv_writer.writerows(data_rows)

# Close the cursor and connection
cursor.close()
conn.close()

print(f"Data from '{table_name}' table has been exported to '{csv_file}' successfully.")
