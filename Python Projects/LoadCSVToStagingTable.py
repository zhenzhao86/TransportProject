##This script uses sql bulk insert to push the csv files into db staging tables

#https://github.com/jiangwen365/pypyodbc
#pip install pypyodbc
import pypyodbc as pyodbc

connection_string = r'' #for using windows auth

db = pyodbc.connect(connection_string)
cursor = db.cursor()
SQL = "BULK INSERT [STAGING_BusStops] FROM 'C:/Users/Administrator/Desktop/ida-dataset/DataSet/12_BusStops.csv' WITH ( FIRSTROW = 2, FIELDTERMINATOR = ',', ROWTERMINATOR = '\n' )"
cursor.execute(SQL)
cursor.commit()
print("Complete Busstops.csv")
SQL = "BULK INSERT [STAGING_12Weekday] FROM 'C:/Users/Administrator/Desktop/ida-dataset/DataSet/12_Weekday_formatted.csv' WITH ( FIRSTROW = 2, FIELDTERMINATOR = ',', ROWTERMINATOR = '\n' )"
cursor.execute(SQL);
cursor.commit()
print("Complete Weekday.csv")
SQL = "BULK INSERT [STAGING_12Sun] FROM 'C:/Users/Administrator/Desktop/ida-dataset/DataSet/12_Sun_formatted.csv' WITH ( FIRSTROW = 2, FIELDTERMINATOR = ',', ROWTERMINATOR = '\n' )"
cursor.execute(SQL)
cursor.commit()
cursor.connection.close()
print("Complete Sun.csv")