import pandas as pd
import pyodbc

data = pd.read_csv (r'/home/jivan/Documents/BOOTCAMP/TEST 1/city_temperature.csv')   
df = pd.DataFrame(data, columns= ['Region','Country','State', 'City', 'Mount', 'Day', 'Year', 'AvgTemperature'])

print(df)

conn = pyodbc.connect(  "host"      : "206.189.80.195",
                        "database"  : "bootcamp",
                        "user"      : "bootcamp",
                        "password"  : "Bootcamp*123")
cursor = conn.cursor()

cursor.execute('CREATE TABLE bootcamp_test_panji (Region text, Country text, State text, City text, Mount int4, Day int4, Year int4, AvgTemperature)')

for row in df.itertuples():
    cursor.execute(''''''''
                INSERT INTO bootcamp.bootcamp_test_panji (Region, Country, State, City, Mount, Day, Year, AvgTemperature)
                VALUES ('','','','','','','','')
                '''''''',
                row.Name, 
                row.Country,
                row.State
                row.City, 
                row.Mount,
                row.Day,
                row.Year, 
                row.AvgTemperature
                )
conn.commit()
