SQL_INSERT_QUERY = "INSERT INTO WeatherByLocation (Longitude,Latitude,forecast_time,Temperature_Celsius,Precipitation_Rate) VALUES (%s, %s, %s,%s,%s)"
SQL_CREATE_TABLE_QUERY = "CREATE TABLE WeatherByLocation (Longitude FLOAT,Latitude FLOAT,forecast_time timestamp ,Temperature_Celsius FLOAT,Precipitation_Rate FLOAT)"
SQL_CREATE_INDEX = "CREATE INDEX WeatherByLocation_idx ON WeatherByLocation (Longitude, Latitude);"
SQL_SELECT_WITH_LON_LAT = "SELECT * FROM WeatherByLocation WHERE Longitude = {0} AND Latitude = {1}"
SQL_SELECT_WITH_OPERATOR = """SELECT 
MAX(Temperature_Celsius),
MAX(Precipitation_Rate),
MIN(Temperature_Celsius),
MIN(Precipitation_Rate),
AVG(Temperature_Celsius),
AVG(Precipitation_Rate)
FROM WeatherByLocation WHERE Longitude = {0} AND Latitude = {1}"""

SQL_DROP_TABLE = "DROP TABLE WeatherByLocation"